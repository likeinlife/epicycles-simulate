from typing import NoReturn

import pygame as pg

from . import drawer
from .enums import Color
from .epicycle_wrapper import EpicycleWrapper
from .settings import Settings
from .types import ColorType


class PyGameWindow:
    def __init__(
        self,
        width: int = 1000,
        height: int = 800,
        fps: int = 60,
        grid_size: int = 20,
        grid_color: ColorType = Color.light_gray,
    ) -> None:
        self.width = width
        self.height = height
        self.grid_size = grid_size
        self.grid_color = grid_color
        self.fps = fps
        self.pause = False

    def main_loop(self) -> NoReturn:
        """
        Entrypoint.

        Starts main loop.
        """
        pg.init()
        self.clock = pg.time.Clock()
        self._init_surfaces()
        self._event_loop()

    def clear_tracers(self) -> None:
        """Clear all tracers."""
        self.tracers_surface.fill(Color.transparent)

    def _init_surfaces(self) -> None:
        self.screen = pg.display.set_mode((self.width, self.height))
        self.screen.fill(Settings.background_color)

        self.background_surface = pg.Surface((self.width, self.height))

        self.tracers_surface = pg.Surface((self.width, self.height), pg.SRCALPHA)
        self.foreground_surface = pg.Surface((self.width, self.height), pg.SRCALPHA)

    def _update_epicycles(self) -> None:
        for wrapper in EpicycleWrapper.wrapper_set:
            previous_pos = wrapper.position.to_tuple()
            wrapper.calculate_next_position()
            current_pos = wrapper.position.to_tuple()

            drawer.draw_epicycle(
                surface=self.foreground_surface,
                tracers_surface=self.tracers_surface,
                epicycle=wrapper.epicycle,
                current_pos=current_pos,
                previous_pos=previous_pos,
                width=self.width,
                height=self.height,
            )

    def _event_loop(self) -> NoReturn:
        while True:
            if not self.pause:
                pg.display.set_caption(str(self.clock.get_fps()))
                self.background_surface.fill(Color.transparent)
                self.foreground_surface.fill(Color.transparent)

                drawer.draw_grid(
                    self.background_surface,
                    self.width,
                    self.height,
                    self.grid_size,
                    self.grid_color,
                )

                self._update_epicycles()

                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        exit()

                self.clock.tick(self.fps)
                self.background_surface.blit(self.tracers_surface, (0, 0))
                self.background_surface.blit(self.foreground_surface, (0, 0))
                self.screen.blit(self.background_surface, (0, 0))

                pg.display.update()
