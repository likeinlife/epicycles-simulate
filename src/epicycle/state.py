from .epicycle_wrapper import EpicycleWrapper


class State:
    selected_wrapper: int | None

    def __init__(
        self,
        pause: bool = False,
        wrapper_list: list[EpicycleWrapper] | None = None,
    ) -> None:
        self.pause = pause
        self.wrappers: dict[int, EpicycleWrapper] = {wrapper.__hash__(): wrapper for wrapper in wrapper_list or []}
        self.selected_wrapper = None
