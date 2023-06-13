import pygame as pg

from . import create_points, drawer
from .config import Colors, Config
from .point import PointCounterMeta

pg.init()
clock = pg.time.Clock()

screen = pg.display.set_mode((Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT))
screen.fill(Colors._BACKGROUND)

background = pg.Surface((Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT))
tracers = pg.Surface((Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT), pg.SRCALPHA)
foreground = pg.Surface((Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT), pg.SRCALPHA)

pause = False


def clear_tracers():
    tracers.fill(Colors._TRANSPARENT)


def event_loop():
    while True:
        if not pause:
            pg.display.set_caption(str(clock.get_fps()))
            background.fill(Colors._TRANSPARENT)
            foreground.fill(Colors._TRANSPARENT)
            drawer.drawGrid(background)

            for _, point in PointCounterMeta.points_list.items():
                drawer.draw_point(foreground, point, tracers)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()

            clock.tick(Config.FPS)
            background.blit(tracers, (0, 0))
            background.blit(foreground, (0, 0))
            screen.blit(background, (0, 0))

            pg.display.update()