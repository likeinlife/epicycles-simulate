import pygame as pg
from pygame.event import Event

from epicycle.commands import DeleteWrapperCommand, ICommand
from epicycle.state import State

from .interface import IHandler


class DeleteWrapperHandler(IHandler):
    @classmethod
    def handle(cls, event: Event, state: State) -> ICommand | None:
        if event.type == pg.KEYDOWN and event.key == pg.K_DELETE:
            return DeleteWrapperCommand(state=state)
        return None
