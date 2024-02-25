from epicycle.epicycle_wrapper import EpicycleWrapper
from epicycle.state import State

from .interface import ICommand


class DeleteSelectedWrapperCommand(ICommand):
    def __init__(self, state: State) -> None:
        self.state = state

    def execute(self) -> None:
        def _del_children(wrapper: EpicycleWrapper) -> None:
            for child in wrapper.children:
                _del_children(child)
                del self.state.wrappers[child.__hash__()]
                del child

        if not self.state.selected_wrapper:
            return None

        wrapper = self.state.wrappers.get(self.state.selected_wrapper)
        if wrapper:
            _del_children(wrapper)
            del self.state.wrappers[wrapper.__hash__()]
            del wrapper

        self.state.selected_wrapper = None
