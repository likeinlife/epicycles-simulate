from epicycle.state import State

from .interface import ICommand


class DeleteSelectedWrapperCommand(ICommand):
    def __init__(self, state: State) -> None:
        self.state = state

    def execute(self) -> None:
        if not self.state.selected_wrapper:
            return None

        wrapper = self.state.wrappers.get(self.state.selected_wrapper)
        if wrapper:
            del self.state.wrappers[wrapper.__hash__()]

        self.state.selected_wrapper = None
