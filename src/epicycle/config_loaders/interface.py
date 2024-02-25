import abc

from epicycle.models import Epicycle


class IConfigLoader(abc.ABC):
    """Interface for config loaders."""

    @abc.abstractmethod
    def load(self) -> list[Epicycle]:
        pass
