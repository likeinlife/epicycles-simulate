from epicycle.state import State

from .interface import ICommand


class SelectWrapperCommand(ICommand):
    def __init__(self, state: State, mouse_position: tuple[int, int]) -> None:
        self.state = state
        self.mouse_position = mouse_position

    def execute(self) -> None:
        print("selecting...")

        def _in(left: float, cur: float, right: float) -> bool:
            return left <= cur <= right

        for wrapper in self.state.wrapper_list:
            if _in(
                wrapper.position.x - wrapper.epicycle.size,
                self.mouse_position[0],
                wrapper.position.x + wrapper.epicycle.size,
            ) and _in(
                wrapper.position.y - wrapper.epicycle.size,
                self.mouse_position[1],
                wrapper.position.y + wrapper.epicycle.size,
            ):
                self.state.selected_wrapper = wrapper.__hash__()
                print(f"selected {self.state.selected_wrapper}")
                break
        else:
            self.state.selected_wrapper = None
