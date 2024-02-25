import pygame as pg
from epicycle.commands import DeleteWrapperCommand, ICommand
from epicycle.state import State
from pygame.event import Event

from .interface import IHandler


class DeleteWrapperHandler(IHandler):
    @classmethod
    def handle(cls, event: Event, state: State) -> ICommand | None:
        if event.type == pg.KEYDOWN and event.key == pg.K_DELETE:
            return DeleteWrapperCommand(state=state)
        return None