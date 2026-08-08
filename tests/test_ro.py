"""Tests for RO core intelligence interface."""

from polyglot import RO


def test_ro_status():
    """Test RO status endpoint."""
    ro = RO()

    status = ro.status()

    assert status["name"] == "RO"
    assert status["status"] == "online"
    assert status["context"] is True
    assert status["memory"] is True


def test_ro_process():
    """Test RO request processing."""
    ro = RO()

    result = ro.process("Hello RO")

    assert result["assistant"] == "RO"
    assert result["request"] == "Hello RO"
    assert result["status"] == "received"


def test_ro_process_strips_whitespace():
    """Test RO strips whitespace from requests."""
    ro = RO()

    result = ro.process("  Hello RO  \n")

    assert result["request"] == "Hello RO"


def test_ro_process_empty_raises():
    """Test RO raises ValueError on empty request."""
    ro = RO()

    try:
        ro.process("")
        assert False, "Expected ValueError"
    except ValueError as e:
        assert "empty" in str(e).lower()


def test_ro_memory():
    """Test RO remember and recall."""
    ro = RO()

    ro.remember("project", "Polyglot AI")

    assert ro.recall("project") == "Polyglot AI"


def test_ro_memory_default():
    """Test RO recall with default value."""
    ro = RO()

    result = ro.recall("nonexistent", "default_value")

    assert result == "default_value"
