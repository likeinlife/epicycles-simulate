import pygame as pg

from .models import Epicycle
from .settings import Settings
from .types import ColorType


def draw_grid(surface: pg.Surface, width: int, height: int, grid_size: int, grid_color: ColorType) -> None:
    """Draw grid over surface."""
    for x in range(0, width, grid_size):
        for y in range(0, height, grid_size):
            rect = pg.Rect(x, y, grid_size, grid_size)
            pg.draw.rect(surface, grid_color, rect, 1)


def draw_epicycle(
    surface: pg.Surface,
    tracers_surface: pg.Surface,
    epicycle: Epicycle,
    previous_pos: tuple[float, float],
    current_pos: tuple[float, float],
    width: int,
    height: int,
    tracer_width: int = 1,
    connect_line_width: int = 1,
) -> None:
    """Draw epicycle and its tracer."""
    if not validate_coordinates(current_pos, width, height):
        return

    if epicycle.has_tracer:
        pg.draw.line(
            tracers_surface,
            epicycle.color,
            previous_pos,
            current_pos,
            tracer_width,
        )

    if epicycle.has_connect_line:
        pg.draw.line(
            surface,
            Settings.connect_color,
            epicycle.center.to_tuple(),
            current_pos,
            connect_line_width,
        )

    if epicycle.visible:
        pg.draw.circle(
            surface,
            epicycle.color,
            current_pos,
            epicycle.size,
        )

    # TODO: Selection mode
    # if wrapper.selected:
    #     if pg.time.get_ticks() % 500 < 300:
    #         pg.draw.circle(
    #             surface,
    #             Settings.connect_color,
    #             wrapper.point.coordinates,
    #             wrapper.size + 50 / wrapper.size,
    #         )


def validate_coordinates(coordinate: tuple[float, float], width: int, height: int) -> bool:
    if 0 <= coordinate[0] <= width and 0 <= coordinate[1] <= height:
        return True
    return False
