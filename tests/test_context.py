"""Tests for context management."""

from polyglot.context.manager import ContextManager


def test_context_session():
    """Test session context."""
    context = ContextManager()

    context.set("name", "RO")

    assert context.get("name") == "RO"


def test_context_persistent():
    """Test persistent context."""
    context = ContextManager()

    context.remember("project", "Polyglot AI")

    assert context.get("project") == "Polyglot AI"


def test_context_session_takes_precedence():
    """Test session context takes precedence over persistent."""
    context = ContextManager()

    context.remember("key", "persistent_value")
    context.set("key", "session_value", persistent=False)

    assert context.get("key") == "session_value"


def test_context_forget():
    """Test forgetting context values."""
    context = ContextManager()

    context.remember("key", "value")
    context.forget("key")

    assert context.get("key") is None


def test_context_snapshot():
    """Test context snapshot."""
    context = ContextManager()

    context.set("session_key", "session_value")
    context.remember("persistent_key", "persistent_value")

    snapshot = context.snapshot()

    assert "session" in snapshot
    assert "persistent" in snapshot
    assert "timestamp" in snapshot
    assert snapshot["session"]["session_key"] == "session_value"
    assert snapshot["persistent"]["persistent_key"] == "persistent_value"


def test_context_get_default():
    """Test context get with default value."""
    context = ContextManager()

    result = context.get("nonexistent", "default")

    assert result == "default"
