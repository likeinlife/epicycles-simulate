from typing import Self

import dearpygui.dearpygui as dpg
from epicycle import State
from epicycle.commands import DeleteSelectedWrapperCommand

from dearpywindow.enums import WindowId

from ..base import BaseWindow
from ..interface import IWindow


class DeleteEpicycleWindow(BaseWindow):
    window_id = WindowId.delete_epicycle

    def __init__(self, state: State, no_wrapper_selected_window: IWindow):
        self.state = state
        self.no_wrapper_selected_window = no_wrapper_selected_window

    def configure(self) -> Self:
        with dpg.window(
            modal=True,
            tag=self.window_id,
            label="Delete epicycle",
        ):
            dpg.add_text(default_value="Delete epicycle")

            dpg.add_button(label="Are you sure?", callback=self._delete_epicycle_handler)

        self.hide()
        return self

    def _delete_epicycle_handler(self) -> None:
        wrapper_id = self.state.selected_wrapper
        if not wrapper_id:
            self.hide()
            self.no_wrapper_selected_window.show()
            return

        DeleteSelectedWrapperCommand(state=self.state).execute()
        self.hide()

    def show(self) -> None:
        wrapper_id = self.state.selected_wrapper
        if not wrapper_id:
            self.hide()
            self.no_wrapper_selected_window.show()
        else:
            super().show()
