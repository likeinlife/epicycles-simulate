from dataclasses import dataclass


class Config:
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 800
    FPS = 120


class Colors:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    MAGENTA = (127, 0, 127)
    BACKGROUND = WHITE

    CONNECT_COLOR = BLACK