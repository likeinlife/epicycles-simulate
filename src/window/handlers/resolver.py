import pygame as pg
from state import State

from window.commands import ICommand

from .delete_wrapper import DeleteWrapperHandler
from .exit_handler import ExitHandler
from .interface import IHandler
from .mouse_click_select import MouseClickSelectHandler
from .pause_handler import PauseHandler

handlers: list[type[IHandler]] = [PauseHandler, ExitHandler, MouseClickSelectHandler, DeleteWrapperHandler]


def resolve_event(event: pg.event.Event, state: State) -> ICommand | None:
    for handler in handlers:
        command = handler.handle(event, state)
        if command:
            return command
    return None
