import pygame as pg
from .config import Colors, Config
from .calculate import Point, Point2D, PointCounterMeta
from . import drawer

pg.init()

screen = pg.display.set_mode((Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT))
screen.fill(Colors.BACKGROUND)
clock = pg.time.Clock()

point1 = Point(Point2D(400, 400), 200, 30, 10, Colors.BLACK)
point2 = point1.create_connected_point(100, 70, 5, Colors.BLUE)
point2.create_connected_point(20, 50, 5, Colors.RED)

point3 = Point(Point2D(200, 200), 100, 100, 40, Colors.GREEN)
point_4 = point3.create_connected_point(300, 150, 20, Colors.BLUE)

point_low_edge = Point(Point2D(Config.SCREEN_WIDTH - 50, Config.SCREEN_HEIGHT - 50), 100, 100, 40, Colors.GREEN)
point_low_edge.create_connected_point(100, 120, 30, Colors.MAGENTA)

print(PointCounterMeta.points_list)


def event_loop():
    while True:
        pg.display.set_caption(str(clock.get_fps()))
        screen.fill(Colors.BACKGROUND)
        for point in PointCounterMeta.points_list:
            if point == point_4:
                print(point.point.coordinates)
            drawer.draw_point(point)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()

        clock.tick(Config.FPS)

        pg.display.update()