from typing import Self

import dearpygui.dearpygui as dpg

from dearpywindow.enums import WindowId

from ..base import BaseWindow


class NoWrapperSelectedErrorWindow(BaseWindow):
    window_id = WindowId.no_wrapper_selected

    def configure(self) -> Self:
        with dpg.window(label="Error", tag=self.window_id, popup=True):
            dpg.add_text("No wrapper selected")
            dpg.add_button(
                label="Ok",
                width=75,
                callback=self.hide,
            )
        return self
