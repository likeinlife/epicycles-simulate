from epicycle.state import State

from .interface import ICommand


class DeselectWrapperCommand(ICommand):
    def __init__(self, state: State) -> None:
        self.state = state

    def execute(self) -> None:
        self.state.selected_wrapper = None
