from typing import Protocol


class PyGameWindow(Protocol):
    def clear_tracers(self) -> None:
        """Clear all tracers."""
