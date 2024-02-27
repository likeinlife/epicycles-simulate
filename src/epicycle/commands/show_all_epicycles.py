from epicycle.state import State

from .interface import ICommand


class ShowAllWrappersEpicycles(ICommand):
    def __init__(self, state: State) -> None:
        self.state = state

    def execute(self) -> None:
        [wrapper.update(visible=True) for wrapper in self.state.wrappers.values()]
