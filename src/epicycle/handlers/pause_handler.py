import pygame as pg
from pygame.event import Event

from epicycle.commands import ICommand, PauseCommand
from epicycle.state import State

from .interface import IHandler


class PauseHandler(IHandler):
    @classmethod
    def handle(cls, event: Event, state: State) -> ICommand | None:
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_p:
                return PauseCommand(state)
        return None
