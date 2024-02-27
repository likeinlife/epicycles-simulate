from typing import Self

import dearpygui.dearpygui as dpg
from epicycle.commands import ShowAllWrappersEpicycles
from epicycle.state import State

from dearpywindow.enums import WindowId

from .base import BaseWindow
from .interface import IWindow


class EpicyclesMenuWindow(BaseWindow):
    window_id = WindowId.epicycles_menu

    def __init__(
        self,
        state: State,
        create_epicycle_window: IWindow,
        update_epicycle_window: IWindow,
        delete_epicycle_window: IWindow,
        create_child_epicycle_window: IWindow,
    ):
        self.state = state
        self.create_epicycle_window = create_epicycle_window
        self.update_epicycle_window = update_epicycle_window
        self.delete_epicycle_window = delete_epicycle_window
        self.create_child_epicycle_window = create_child_epicycle_window

    def configure(self) -> Self:
        with dpg.window(tag=self.window_id, label="List Points", autosize=True):
            dpg.add_text("Epicycle menu")

            dpg.add_button(label="Create epicycle", callback=self.create_epicycle_window.show)
            dpg.add_button(label="Update epicycle", callback=self.update_epicycle_window.show)
            dpg.add_button(label="Delete epicycle", callback=self.delete_epicycle_window.show)
            dpg.add_button(label="Create child epicycle", callback=self.create_child_epicycle_window.show)
            dpg.add_button(label="Show all epicycles", callback=ShowAllWrappersEpicycles(self.state).execute)
            dpg.add_button(label="Hide panel", callback=self.hide)

        self.hide()
        return self
