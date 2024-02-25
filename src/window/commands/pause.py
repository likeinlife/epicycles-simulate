from state import State

from .interface import ICommand


class PauseCommand(ICommand):
    def __init__(self, state: State) -> None:
        self.state = state

    def execute(self) -> None:
        self.state.pause = not self.state.pause
