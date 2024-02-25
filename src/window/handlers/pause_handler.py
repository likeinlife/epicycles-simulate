import pygame as pg
from epicycle.state import State
from pygame.event import Event

from window.commands import ICommand, PauseCommand

from .interface import IHandler


class PauseHandler(IHandler):
    @classmethod
    def handle(cls, event: Event, state: State) -> ICommand | None:
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_p:
                return PauseCommand(state)
        return None
