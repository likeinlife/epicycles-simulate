import pygame as pg

from epicycle.commands import ICommand
from epicycle.handlers.mouse_click_select import MouseClickSelectHandler
from epicycle.state import State

from .exit_handler import ExitHandler
from .interface import IHandler
from .pause_handler import PauseHandler

handlers: list[type[IHandler]] = [PauseHandler, ExitHandler, MouseClickSelectHandler]


def resolve_event(event: pg.event.Event, state: State) -> ICommand | None:
    for handler in handlers:
        command = handler.handle(event, state)
        if command:
            return command
    return None
