"""Abstract base class for agents."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class Agent(ABC):
    """Abstract base class for agents."""

    name: str = "agent"

    @abstractmethod
    def run(
        self,
        task: str,
        context: dict[str, Any] | None = None,
    ) -> Any:
        """Execute an agent task.

        Args:
            task: The task description or instruction.
            context: Optional context dictionary for the task.

        Returns:
            Task result or output.

        Raises:
            NotImplementedError: Subclasses must implement this method.
        """
        raise NotImplementedError
