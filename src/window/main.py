from epicycle.state import State
from type_alias import ColorType

from .enums import Color
from .window import PyGameWindow


def start(
    state: State,
    width: int = 1000,
    height: int = 800,
    fps: int = 60,
    grid_size: int = 20,
    grid_color: ColorType = Color.light_gray,
):
    window = PyGameWindow(
        state=state,
        width=width,
        height=height,
        fps=fps,
        grid_size=grid_size,
        grid_color=grid_color,
    )
    window.main_loop()
