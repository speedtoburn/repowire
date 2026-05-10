"""Tests for spawn_hints module."""

from __future__ import annotations

import time
from pathlib import Path

import pytest

from repowire import spawn_hints
from repowire.spawn_hints import consume_hint, write_hint


@pytest.fixture
def tmp_cache(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    """Redirect spawn_hints to a temp cache dir."""
    monkeypatch.setattr("repowire.spawn_hints.CACHE_DIR", tmp_path)
    return tmp_path


def test_write_then_consume_returns_circle(tmp_cache: Path) -> None:
    write_hint("/tmp/proj", "codex", "5")
    hint = consume_hint("/tmp/proj", "codex")
    assert hint is not None
    assert hint.circle == "5"
    assert hint.pane_id is None


def test_write_with_pane_id_round_trips(tmp_cache: Path) -> None:
    write_hint("/tmp/proj", "codex", "5", pane_id="%42")
    hint = consume_hint("/tmp/proj", "codex")
    assert hint is not None
    assert hint.circle == "5"
    assert hint.pane_id == "%42"


def test_consume_deletes_hint(tmp_cache: Path) -> None:
    write_hint("/tmp/proj", "codex", "5")
    consume_hint("/tmp/proj", "codex")
    assert consume_hint("/tmp/proj", "codex") is None


def test_consume_missing_returns_none(tmp_cache: Path) -> None:
    assert consume_hint("/tmp/never-spawned", "codex") is None


def test_hints_keyed_by_path_and_backend(tmp_cache: Path) -> None:
    write_hint("/tmp/proj", "codex", "5")
    write_hint("/tmp/proj", "claude-code", "7")
    h_codex = consume_hint("/tmp/proj", "codex")
    h_claude = consume_hint("/tmp/proj", "claude-code")
    assert h_codex is not None and h_codex.circle == "5"
    assert h_claude is not None and h_claude.circle == "7"


def test_stale_hint_returns_none_and_is_deleted(
    tmp_cache: Path, monkeypatch: pytest.MonkeyPatch,
) -> None:
    write_hint("/tmp/proj", "codex", "5")
    # Fast-forward time past the TTL.
    future = time.time() + 9999
    fake_time = type("T", (), {"time": staticmethod(lambda: future)})
    monkeypatch.setattr(spawn_hints, "time", fake_time)
    assert consume_hint("/tmp/proj", "codex") is None
    # Calling again should still return None (file already deleted).
    assert consume_hint("/tmp/proj", "codex") is None


def test_corrupt_hint_returns_none(tmp_cache: Path) -> None:
    hints_dir = tmp_cache / "spawn-hints"
    hints_dir.mkdir(parents=True, exist_ok=True)
    write_hint("/tmp/proj", "codex", "5")
    # Corrupt the file.
    target = next(hints_dir.glob("*.json"))
    target.write_text("not json{")
    assert consume_hint("/tmp/proj", "codex") is None


def test_path_resolved_so_equivalent_paths_match(tmp_cache: Path, tmp_path: Path) -> None:
    real = tmp_path / "proj"
    real.mkdir()
    write_hint(str(real), "codex", "5")
    # Same path with a redundant segment that resolve() will normalize.
    hint = consume_hint(str(real / "." ), "codex")
    assert hint is not None and hint.circle == "5"
