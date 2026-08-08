"""RO — Core intelligent interface for Polyglot AI."""

from __future__ import annotations

from typing import Any

from polyglot.context.manager import ContextManager
from polyglot.memory.store import MemoryStore


class RO:
    """Core intelligent interface for Polyglot AI.

    RO combines persistent context, memory, and coordination capabilities
    to provide a unified AI platform for ongoing project work.
    """

    name = "RO"
    version = "0.1.0"

    def __init__(
        self,
        context: ContextManager | None = None,
        memory: MemoryStore | None = None,
    ) -> None:
        """Initialize RO with optional context and memory.

        Args:
            context: ContextManager instance (creates new if None).
            memory: MemoryStore instance (creates new if None).
        """
        self.context = context or ContextManager()
        self.memory = memory or MemoryStore()

    def remember(self, key: str, value: Any) -> None:
        """Remember a value in both context and persistent memory.

        Args:
            key: The memory key.
            value: The value to remember.
        """
        self.context.remember(key, value)
        self.memory.remember(key, value)

    def recall(self, key: str, default: Any = None) -> Any:
        """Recall a value from context or persistent memory.

        Args:
            key: The memory key.
            default: Default value if key not found.

        Returns:
            The remembered value or default.
        """
        value = self.context.get(key)

        if value is not None:
            return value

        return self.memory.recall(key, default)

    def status(self) -> dict[str, Any]:
        """Get RO status and capabilities.

        Returns:
            Dictionary with status information.
        """
        return {
            "name": self.name,
            "version": self.version,
            "status": "online",
            "context": True,
            "memory": True,
        }

    def process(self, request: str) -> dict[str, Any]:
        """Process an incoming request.

        Args:
            request: User request or instruction.

        Returns:
            Dictionary with processing status.

        Raises:
            ValueError: If request is empty.
        """
        request = request.strip()

        if not request:
            raise ValueError("Request cannot be empty.")

        return {
            "assistant": self.name,
            "request": request,
            "status": "received",
        }
