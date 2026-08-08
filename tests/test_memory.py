"""Tests for memory storage."""

from polyglot.memory.store import MemoryStore


def test_memory_store(tmp_path):
    """Test memory store save and recall."""
    store = MemoryStore(tmp_path / "memory.json")

    store.remember("project", "Polyglot AI")

    assert store.recall("project") == "Polyglot AI"


def test_memory_store_persist(tmp_path):
    """Test memory persists across instances."""
    path = tmp_path / "memory.json"

    store1 = MemoryStore(path)
    store1.remember("key", "value")

    store2 = MemoryStore(path)
    assert store2.recall("key") == "value"


def test_memory_store_forget(tmp_path):
    """Test forgetting memory."""
    store = MemoryStore(tmp_path / "memory.json")

    store.remember("key", "value")
    store.forget("key")

    assert store.recall("key") is None


def test_memory_store_default(tmp_path):
    """Test memory recall with default."""
    store = MemoryStore(tmp_path / "memory.json")

    result = store.recall("nonexistent", "default")

    assert result == "default"


def test_memory_store_creates_directory(tmp_path):
    """Test memory store creates parent directories."""
    store = MemoryStore(tmp_path / "nested" / "dir" / "memory.json")

    store.remember("key", "value")

    assert (tmp_path / "nested" / "dir" / "memory.json").exists()


def test_memory_store_empty(tmp_path):
    """Test memory store with no saved data."""
    store = MemoryStore(tmp_path / "memory.json")

    result = store.load()

    assert result == {}


def test_memory_store_multiple_keys(tmp_path):
    """Test storing multiple keys."""
    store = MemoryStore(tmp_path / "memory.json")

    store.remember("key1", "value1")
    store.remember("key2", "value2")
    store.remember("key3", "value3")

    assert store.recall("key1") == "value1"
    assert store.recall("key2") == "value2"
    assert store.recall("key3") == "value3"
