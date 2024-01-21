class Config:
    SCREEN_WIDTH = 1400
    SCREEN_HEIGHT = 800
    FPS = 120
    GRID_SIDE = 20


class Colors:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (127, 127, 127)
    LIGHT_GRAY = (170, 170, 170)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    MAGENTA = (127, 0, 127)
    CYAN = (0, 127, 127)

    _BACKGROUND = WHITE
    _TRANSPARENT = (255, 255, 255, 0)
    _GRID_COLOR = LIGHT_GRAY

    _CONNECT_COLOR = BLACK
    _SELECT_COLOR = (150, 50, 150)

    @classmethod
    def get_colors(cls) -> list[str]:
        return [
            color
            for color in cls.__dict__
            if color.isupper() and not color.startswith("_")
        ]

    @classmethod
    def find_color_by_value(cls, color_value: tuple) -> str:
        """color_value = '(0, 0, 0)'"""
        colors = cls.get_colors()
        for color in colors:
            if getattr(cls, color) == color_value:
                return color
        raise IndexError("Incorrect color")

    @classmethod
    def get_color(cls, color: str) -> tuple[int, int, int]:
        return getattr(cls, color)
