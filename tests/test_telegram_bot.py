"""Unit tests for Telegram bot keyboard helpers + routing logic."""

from __future__ import annotations

import time

from repowire.telegram.bot import (
    CLEAR_LABEL,
    CURRENT_MARK,
    CURRENT_OFF_MARK,
    MORE_LABEL,
    PEERS_LABEL,
    RECENT_MARK,
    PendingRetry,
    build_reply_keyboard,
    compute_visible_recents,
    parse_keyboard_tap,
)

# -- compute_visible_recents --


def test_recents_preserves_newest_first_order():
    recents = ["c", "b", "a"]
    online = {"a", "b", "c"}
    assert compute_visible_recents(recents, online, current=None) == ["c", "b", "a"]


def test_recents_filters_offline_peers():
    recents = ["c", "b", "a"]
    online = {"a", "c"}
    assert compute_visible_recents(recents, online, current=None) == ["c", "a"]


def test_recents_excludes_current_peer():
    recents = ["c", "b", "a"]
    online = {"a", "b", "c"}
    assert compute_visible_recents(recents, online, current="b") == ["c", "a"]


def test_recents_dedups_repeated_names():
    recents = ["a", "b", "a", "c", "b"]
    online = {"a", "b", "c"}
    assert compute_visible_recents(recents, online, current=None) == ["a", "b", "c"]


def test_recents_honors_limit():
    recents = ["e", "d", "c", "b", "a"]
    online = {"a", "b", "c", "d", "e"}
    assert compute_visible_recents(recents, online, current=None, limit=3) == ["e", "d", "c"]


# -- build_reply_keyboard --


def test_keyboard_marks_current_online():
    kb = build_reply_keyboard(current="torale", recents=[], online={"torale"})
    first_button = kb["keyboard"][0][0]["text"]
    assert first_button == f"{CURRENT_MARK} torale"
    assert kb["input_field_placeholder"] == "msg @torale..."


def test_keyboard_marks_current_offline():
    kb = build_reply_keyboard(current="torale", recents=[], online=set())
    first_button = kb["keyboard"][0][0]["text"]
    assert first_button == f"{CURRENT_OFF_MARK} torale"
    assert "offline" in kb["input_field_placeholder"]


def test_keyboard_no_current_shows_empty_placeholder():
    kb = build_reply_keyboard(current=None, recents=[], online=set())
    assert "No active peer" in kb["input_field_placeholder"]


def test_keyboard_recents_appear_after_current():
    kb = build_reply_keyboard(
        current="torale",
        recents=["orch", "repowire"],
        online={"torale", "orch", "repowire"},
    )
    labels = [btn["text"] for row in kb["keyboard"] for btn in row]
    assert labels[0] == f"{CURRENT_MARK} torale"
    assert labels[1] == f"{RECENT_MARK} orch"
    assert labels[2] == f"{RECENT_MARK} repowire"


def test_keyboard_always_has_commands_row():
    kb = build_reply_keyboard(current=None, recents=[], online=set())
    last_row_labels = [btn["text"] for btn in kb["keyboard"][-1]]
    assert PEERS_LABEL in last_row_labels
    assert CLEAR_LABEL in last_row_labels
    assert MORE_LABEL in last_row_labels


def test_keyboard_pending_retry_placeholder():
    kb = build_reply_keyboard(
        current="torale",
        recents=[],
        online={"torale"},
        pending_retry_text="do option B",
    )
    assert "retry" in kb["input_field_placeholder"]
    assert "do option B" in kb["input_field_placeholder"]


def test_keyboard_pending_retry_truncates_long_text():
    long_text = "x" * 100
    kb = build_reply_keyboard(
        current=None,
        recents=[],
        online=set(),
        pending_retry_text=long_text,
    )
    assert "…" in kb["input_field_placeholder"]
    assert len(kb["input_field_placeholder"]) < 60


def test_keyboard_is_persistent_and_resized():
    kb = build_reply_keyboard(current=None, recents=[], online=set())
    assert kb["is_persistent"] is True
    assert kb["resize_keyboard"] is True


# -- parse_keyboard_tap --


def test_parse_current_peer_tap():
    assert parse_keyboard_tap(f"{CURRENT_MARK} torale") == ("select", "torale")


def test_parse_current_offline_peer_tap():
    assert parse_keyboard_tap(f"{CURRENT_OFF_MARK} torale") == ("select", "torale")


def test_parse_recent_peer_tap():
    assert parse_keyboard_tap(f"{RECENT_MARK} orch") == ("select", "orch")


def test_parse_peers_label():
    assert parse_keyboard_tap(PEERS_LABEL) == ("peers", None)


def test_parse_clear_label():
    assert parse_keyboard_tap(CLEAR_LABEL) == ("clear", None)


def test_parse_more_label():
    assert parse_keyboard_tap(MORE_LABEL) == ("more", None)


def test_parse_plain_text_is_text():
    assert parse_keyboard_tap("hello there") == ("text", None)


def test_parse_at_mention_is_text():
    # @-prefixed text should fall through to the @peer regex path, not be a tap
    assert parse_keyboard_tap("@torale do it") == ("text", None)


def test_parse_marker_alone_without_name_is_text():
    assert parse_keyboard_tap(CURRENT_MARK) == ("text", None)
    assert parse_keyboard_tap(f"{CURRENT_MARK} ") == ("text", None)


# -- PendingRetry TTL --


def test_pending_retry_active_within_window():
    now = time.monotonic()
    r = PendingRetry(text="hi", expires_at=now + 10)
    assert r.is_active(now) is True
    assert r.is_active(now + 5) is True


def test_pending_retry_expired_after_window():
    now = time.monotonic()
    r = PendingRetry(text="hi", expires_at=now + 10)
    assert r.is_active(now + 11) is False


def test_pending_retry_exactly_at_expiry_is_inactive():
    now = time.monotonic()
    r = PendingRetry(text="hi", expires_at=now + 10)
    assert r.is_active(now + 10) is False
