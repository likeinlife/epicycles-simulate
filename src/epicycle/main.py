from .enums import Color
from .types import ColorType


def start(
    width: int = 1000,
    height: int = 800,
    fps: int = 60,
    grid_size: int = 20,
    grid_color: ColorType = Color.light_gray,
):
    from .create_points import create_points
    from .window import PyGameWindow

    state = create_points()
    window = PyGameWindow(
        state=state,
        width=width,
        height=height,
        fps=fps,
        grid_size=grid_size,
        grid_color=grid_color,
    )
    window.main_loop()
