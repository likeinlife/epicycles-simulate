from dataclasses import dataclass


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
    BACKGROUND = WHITE
    TRANSPARENT = (255, 255, 255, 0)
    GRID_COLOR = LIGHT_GRAY

    CONNECT_COLOR = BLACK