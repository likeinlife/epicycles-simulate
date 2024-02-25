import abc

import pygame as pg
from state import State

from epicycle.commands import ICommand


class IHandler(abc.ABC):
    @classmethod
    @abc.abstractmethod
    def handle(cls, event: pg.event.Event, state: State) -> ICommand | None:
        ...
