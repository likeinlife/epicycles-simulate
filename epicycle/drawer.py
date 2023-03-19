from .calculate import Point, Point2D
import pygame as pg
from epicycle.config import Colors, Config


def drawGrid(surface):
    for x in range(0, Config.SCREEN_WIDTH, Config.GRID_SIDE):
        for y in range(0, Config.SCREEN_HEIGHT, Config.GRID_SIDE):
            rect = pg.Rect(x, y, Config.GRID_SIDE, Config.GRID_SIDE)
            pg.draw.rect(surface, Colors.GRID_COLOR, rect, 1)


def draw_point(surface, point: Point, tracers_surface):
    first_point = point.point.coordinates
    if validate_coordinates(point.point):
        pg.draw.circle(surface, Colors.TRANSPARENT, point.point.coordinates, point.size)
    point.calculate_next_point_pos()
    pg.draw.line(surface, Colors.CONNECT_COLOR, point.point.coordinates, point.center.coordinates)
    if validate_coordinates(point.point):
        second_point = point.point.coordinates
        pg.draw.line(tracers_surface, point.color, first_point, second_point, 2)
        pg.draw.circle(surface, point.color, point.point.coordinates, point.size)


def validate_coordinates(coordinates: Point2D) -> bool:
    if 0 <= coordinates.x <= Config.SCREEN_WIDTH:
        if 0 <= coordinates.y <= Config.SCREEN_HEIGHT:
            return True
    return False
