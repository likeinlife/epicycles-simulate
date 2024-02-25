import dearpygui.dearpygui as dpg

from .interface import IWindow


class BaseWindow(IWindow):
    def hide(self) -> None:
        dpg.hide_item(self.window_id)

    def show(self) -> None:
        dpg.show_item(self.window_id)
