import pygame as pg
from epicycle.state import State
from pygame.event import Event

from window.commands import ExitCommand, ICommand

from .interface import IHandler


class ExitHandler(IHandler):
    @classmethod
    def handle(cls, event: Event, state: State) -> ICommand | None:
        if event.type == pg.QUIT:
            return ExitCommand()
        return None
