import abc
from typing import Self

from dearpywindow.enums import WindowId


class IWindow(abc.ABC):
    """Interface for windows."""

    window_id: WindowId

    @abc.abstractmethod
    def configure(self) -> Self:
        """Configure window."""

    @abc.abstractmethod
    def show(self) -> None:
        """Show window."""

    @abc.abstractmethod
    def hide(self) -> None:
        """Hide window."""
