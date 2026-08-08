"""Context manager for persistent and session context."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any


@dataclass
class ContextManager:
    """Manages session and persistent context."""

    session: dict[str, Any] = field(default_factory=dict)
    persistent: dict[str, Any] = field(default_factory=dict)

    def set(self, key: str, value: Any, persistent: bool = False) -> None:
        """Set a context value."""
        target = self.persistent if persistent else self.session
        target[key] = value

    def get(self, key: str, default: Any = None) -> Any:
        """Get a context value (session takes precedence)."""
        if key in self.session:
            return self.session[key]
        return self.persistent.get(key, default)

    def remember(self, key: str, value: Any) -> None:
        """Store a value in persistent context."""
        self.persistent[key] = value

    def forget(self, key: str) -> None:
        """Remove a key from both session and persistent context."""
        self.session.pop(key, None)
        self.persistent.pop(key, None)

    def snapshot(self) -> dict[str, Any]:
        """Capture a snapshot of current context state."""
        return {
            "session": dict(self.session),
            "persistent": dict(self.persistent),
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }
