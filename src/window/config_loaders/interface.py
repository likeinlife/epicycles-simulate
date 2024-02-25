import abc

from window.models import Epicycle


class IConfigLoader(abc.ABC):
    """Interface for config loaders."""

    @abc.abstractmethod
    def load(self) -> list[Epicycle]:
        pass
