from epicycle.state import State
from type_alias import ColorType

from .enums import Color
from .window import PyGameWindow


def create_window(
    state: State,
    width: int = 1000,
    height: int = 800,
    grid_size: int = 20,
    grid_color: ColorType = Color.light_gray,
):
    window = PyGameWindow(
        state=state,
        width=width,
        height=height,
        grid_size=grid_size,
        grid_color=grid_color,
    )
    return window


def start(
    window: PyGameWindow,
):
    window.main_loop()
