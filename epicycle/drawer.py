from .calculate import Point, Point2D
import pygame as pg
from epicycle.config import Colors, Config


def draw_point(point: Point):
    from .window import screen
    point.calculate_next_point_pos()
    pg.draw.line(screen, Colors.CONNECT_COLOR, point.point.coordinates, point.center.coordinates)
    if validate_coordinates(point.point):
        pg.draw.circle(screen, point.color, point.point.coordinates, point.size)


def validate_coordinates(coordinates: Point2D) -> bool:
    if 0 <= coordinates.x <= Config.SCREEN_WIDTH:
        if 0 <= coordinates.y <= Config.SCREEN_HEIGHT:
            return True
    return False
