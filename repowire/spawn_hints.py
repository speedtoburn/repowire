"""Spawn hint files: bridge spawn intent to runtimes that strip tmux env.

When the daemon spawns a peer via /spawn, the requested circle is encoded only
as the tmux session name. Most runtimes (Claude Code, Gemini) inherit TMUX env
into MCP/hook subprocesses, so they can read the session name back from
`tmux display-message`. Codex sandboxes its MCP and hook subprocesses with a
minimal env (no TMUX, TMUX_PANE, PWD), so it cannot recover the session name —
the eager `_ensure_registered` and the SessionStart hook both fall back to
circle="default".

To bridge that gap, the spawn flow drops a small JSON hint file under
`~/.cache/repowire/spawn-hints/` keyed by (path, backend). Registration
fallbacks consult this hint before falling back to "default" and consume it
on use. Hints have a short TTL so stale ones never override later spawns.
"""

from __future__ import annotations

import hashlib
import json
import logging
import time
from contextlib import suppress
from dataclasses import dataclass
from pathlib import Path

from repowire.config.models import CACHE_DIR

logger = logging.getLogger(__name__)


@dataclass
class Hint:
    """Spawn intent recovered for a (path, backend) pair."""

    circle: str
    pane_id: str | None = None

# Hints older than this are ignored and treated as garbage. Spawn → MCP boot
# → eager register usually completes within a few seconds; 5 minutes is
# generous slack for slow hosts and codex's late-fired SessionStart.
HINT_TTL_SECONDS = 300


def _hints_dir() -> Path:
    path = CACHE_DIR / "spawn-hints"
    path.mkdir(parents=True, exist_ok=True)
    return path


def _hint_key(path: str, backend: str) -> str:
    raw = f"{Path(path).resolve()}::{backend}".encode()
    return hashlib.sha256(raw).hexdigest()[:16]


def _hint_path(path: str, backend: str) -> Path:
    return _hints_dir() / f"{_hint_key(path, backend)}.json"


def write_hint(
    path: str, backend: str, circle: str, pane_id: str | None = None,
) -> None:
    """Record spawn intent so a peer registering from this path+backend can
    discover its requested circle and (when the runtime strips tmux env)
    its tmux pane.
    """
    payload: dict = {
        "path": str(Path(path).resolve()),
        "backend": backend,
        "circle": circle,
        "ts": time.time(),
    }
    if pane_id:
        payload["pane_id"] = pane_id
    target = _hint_path(path, backend)
    try:
        target.write_text(json.dumps(payload))
    except OSError as e:
        logger.warning("spawn_hints: failed to write %s: %s", target, e)


def consume_hint(path: str, backend: str) -> Hint | None:
    """Read and delete the spawn hint for (path, backend).

    Returns the recovered Hint (circle + optional pane_id), or None if no
    fresh hint exists. Stale hints (older than HINT_TTL_SECONDS) are deleted
    and treated as missing.
    """
    target = _hint_path(path, backend)
    try:
        raw = target.read_text()
    except OSError:
        return None

    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        with suppress(OSError):
            target.unlink()
        return None

    ts = data.get("ts")
    circle = data.get("circle")
    if not isinstance(ts, (int, float)) or not isinstance(circle, str):
        with suppress(OSError):
            target.unlink()
        return None

    age = time.time() - ts
    with suppress(OSError):
        target.unlink()

    if age > HINT_TTL_SECONDS:
        return None
    pane_id = data.get("pane_id") if isinstance(data.get("pane_id"), str) else None
    return Hint(circle=circle, pane_id=pane_id)
