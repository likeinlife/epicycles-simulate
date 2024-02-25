import abc

import pygame as pg

from epicycle.commands import ICommand
from epicycle.state import State


class IHandler(abc.ABC):
    @classmethod
    @abc.abstractmethod
    def handle(cls, event: pg.event.Event, state: State) -> ICommand | None:
        ...
