import pygame as pg
from pygame.event import Event
from state import State

from window.commands import ICommand, SelectWrapperCommand

from .interface import IHandler


class MouseClickSelectHandler(IHandler):
    @classmethod
    def handle(cls, event: Event, state: State) -> ICommand | None:
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                return SelectWrapperCommand(state, event.pos)
        return None
