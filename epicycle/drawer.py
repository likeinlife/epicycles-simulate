import pygame as pg

from epicycle.config import Colors, Config

from .point import Point, Point2D


def drawGrid(surface):
    for x in range(0, Config.SCREEN_WIDTH, Config.GRID_SIDE):
        for y in range(0, Config.SCREEN_HEIGHT, Config.GRID_SIDE):
            rect = pg.Rect(x, y, Config.GRID_SIDE, Config.GRID_SIDE)
            pg.draw.rect(surface, Colors._GRID_COLOR, rect, 1)


def draw_point(surface, point: Point, tracers_surface):
    first_point = point.point.coordinates

    point.calculate_next_point_pos()
    if validate_coordinates(point.point):
        second_point = point.point.coordinates
        if point.need_to_draw_tracer:  # tracer
            pg.draw.line(tracers_surface, point.color, first_point, second_point, 2)
        if point.need_to_draw_connecting_line:  # connecting line
            pg.draw.line(surface, Colors._CONNECT_COLOR, point.point.coordinates, point.center.coordinates)
        if point.visible:  # point
            pg.draw.circle(surface, point.color, point.point.coordinates, point.size)
        if point.selected:
            if pg.time.get_ticks() % 500 < 300:
                pg.draw.circle(surface, Colors._SELECT_COLOR, point.point.coordinates, point.size + 50 / point.size)


def validate_coordinates(coordinates: Point2D) -> bool:
    if 0 <= coordinates.x <= Config.SCREEN_WIDTH:
        if 0 <= coordinates.y <= Config.SCREEN_HEIGHT:
            return True
    return False
