import abc


class IConfigDumper(abc.ABC):
    @abc.abstractmethod
    def dump(self):
        pass
