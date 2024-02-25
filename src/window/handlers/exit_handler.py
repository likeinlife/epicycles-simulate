import pygame as pg
from pygame.event import Event
from state import State

from window.commands import ExitCommand, ICommand

from .interface import IHandler


class ExitHandler(IHandler):
    @classmethod
    def handle(cls, event: Event, state: State) -> ICommand | None:
        if event.type == pg.QUIT:
            return ExitCommand()
        return None
