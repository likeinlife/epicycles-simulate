import pygame as pg

from . import create_points
from .config import Colors, Config
from .calculate import PointCounterMeta
from . import drawer

pg.init()
clock = pg.time.Clock()

screen = pg.display.set_mode((Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT))
screen.fill(Colors.BACKGROUND)

background = pg.Surface((Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT))
tracers = pg.Surface((Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT), pg.SRCALPHA)
foreground = pg.Surface((Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT), pg.SRCALPHA)


def event_loop():
    while True:
        pg.display.set_caption(str(clock.get_fps()))
        background.fill(Colors.TRANSPARENT)
        foreground.fill(Colors.TRANSPARENT)
        drawer.drawGrid(background)

        for point in PointCounterMeta.points_list:
            drawer.draw_point(foreground, point, tracers)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()

        clock.tick(Config.FPS)
        background.blit(tracers, (0, 0))
        background.blit(foreground, (0, 0))
        screen.blit(background, (0, 0))

        pg.display.update()