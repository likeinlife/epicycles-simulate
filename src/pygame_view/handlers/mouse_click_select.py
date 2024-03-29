import pygame as pg
from epicycle.commands import ICommand, SelectWrapperCommand
from epicycle.state import State
from pygame.event import Event

from .interface import IHandler


class MouseClickSelectHandler(IHandler):
    @classmethod
    def handle(cls, event: Event, state: State) -> ICommand | None:
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                return SelectWrapperCommand(state, event.pos)
        return None
