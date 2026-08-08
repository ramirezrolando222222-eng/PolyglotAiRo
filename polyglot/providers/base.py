"""Abstract base class for AI providers."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class AIProvider(ABC):
    """Abstract interface for AI model providers."""

    @abstractmethod
    def generate(
        self,
        prompt: str,
        **kwargs: Any,
    ) -> str:
        """Generate a response from an AI provider.

        Args:
            prompt: The input prompt for generation.
            **kwargs: Additional provider-specific parameters.

        Returns:
            Generated response text.

        Raises:
            NotImplementedError: Subclasses must implement this method.
        """
        raise NotImplementedError
