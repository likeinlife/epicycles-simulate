from .epicycle_wrapper import EpicycleWrapper


class State:
    selected_wrapper: int | None

    def __init__(
        self,
        pause: bool = False,
        wrappers: list[EpicycleWrapper] | None = None,
    ) -> None:
        self.pause = pause
        self.wrapper_list = wrappers or []
        self.selected_wrapper = None
