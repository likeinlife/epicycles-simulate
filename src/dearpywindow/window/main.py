from enum import Enum
from typing import Self

import dearpygui.dearpygui as dpg
from epicycle.commands.delete_all_wrappers import DeleteAllWrappersCommand
from epicycle.commands.deselect_wrapper import DeselectWrapperCommand
from epicycle.commands.pause import PauseCommand
from epicycle.state import State

from dearpywindow import actions
from dearpywindow.enums import WindowId
from dearpywindow.protocols import PyGameWindow
from dearpywindow.window.interface import IWindow

from .base import BaseWindow


class MenuElementEnum(str, Enum):
    load_file = "load_file"


class MainWindow(BaseWindow):
    window_id = WindowId.main

    def __init__(self, state: State, epicycles_menu: IWindow, pygame_window: PyGameWindow):
        self.state = state
        self.epicycles_menu = epicycles_menu
        self.pygame_window = pygame_window

    def configure(self) -> Self:
        with dpg.window(label="Epicycles", tag=self.window_id):
            dpg.add_button(
                label="Points",
                callback=self.epicycles_menu.show,
            )
            dpg.add_button(
                label="Clear selection",
                callback=DeselectWrapperCommand(self.state).execute,
            )

            with dpg.group(horizontal=True):
                dpg.add_button(label="Clear objects", callback=DeleteAllWrappersCommand(self.state).execute)
                dpg.add_button(label="||", callback=PauseCommand(self.state).execute)
                dpg.add_button(label="Clear tracers", callback=self.pygame_window.clear_tracers)

            with dpg.file_dialog(
                label="Load Json config",
                show=False,
                directory_selector=False,
                callback=lambda: actions.load_json_config(MenuElementEnum.load_file),
                tag=MenuElementEnum.load_file,
                width=700,
                height=400,
            ):
                dpg.add_file_extension(".json", color=(70, 200, 70, 255))

            dpg.add_button(label="Load json config", callback=lambda: dpg.show_item(MenuElementEnum.load_file))

            # with dpg.file_dialog(
            #     label="Dump config to json",
            #     show=False,
            #     directory_selector=False,
            #     callback=menu_actions.dump_json_callback,
            #     cancel_callback=menu_actions.dump_json_cancel_callback,
            #     tag="dump_file",
            #     width=700,
            #     height=400,
            # ):
            #     dpg.add_file_extension(".json", color=(70, 200, 70, 255))

            # dpg.add_button(label="Dump config to json", callback=lambda: dpg.show_item("dump_file"))
        return self
