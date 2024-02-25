import abc
from typing import NoReturn


class IPyGameWindow(abc.ABC):
    @abc.abstractmethod
    def main_loop(self) -> NoReturn:
        """
        Entrypoint.

        Starts main loop.
        """
        ...

    @abc.abstractmethod
    def clear_tracers(self) -> None:
        """Clear all tracers."""
