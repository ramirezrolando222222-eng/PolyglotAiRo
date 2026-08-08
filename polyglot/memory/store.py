"""Persistent memory storage for RO."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


class MemoryStore:
    """Persistent JSON-based memory storage."""

    def __init__(self, path: str | Path = "data/ro_memory.json") -> None:
        """Initialize memory store with a file path."""
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def load(self) -> dict[str, Any]:
        """Load all memories from storage."""
        if not self.path.exists():
            return {}

        try:
            return json.loads(self.path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            return {}

    def save(self, data: dict[str, Any]) -> None:
        """Save memories to storage."""
        self.path.write_text(
            json.dumps(data, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )

    def remember(self, key: str, value: Any) -> None:
        """Store a memory."""
        data = self.load()
        data[key] = value
        self.save(data)

    def recall(self, key: str, default: Any = None) -> Any:
        """Retrieve a memory."""
        return self.load().get(key, default)

    def forget(self, key: str) -> None:
        """Remove a memory."""
        data = self.load()
        data.pop(key, None)
        self.save(data)
