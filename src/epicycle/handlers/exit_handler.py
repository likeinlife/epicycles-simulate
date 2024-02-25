import pygame as pg
from pygame.event import Event

from epicycle.commands import ExitCommand, ICommand
from epicycle.state import State

from .interface import IHandler


class ExitHandler(IHandler):
    @classmethod
    def handle(cls, event: Event, state: State) -> ICommand | None:
        if event.type == pg.QUIT:
            return ExitCommand()
        return None
