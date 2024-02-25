from .interface import ICommand


class ExitCommand(ICommand):
    def execute(self) -> None:
        exit()
