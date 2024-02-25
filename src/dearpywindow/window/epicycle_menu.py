from typing import Self

import dearpygui.dearpygui as dpg
from epicycle.state import State

from dearpywindow.enums import WindowId

from .base import BaseWindow
from .interface import IWindow


class EpicyclesMenuWindow(BaseWindow):
    window_id = WindowId.epicycles_menu

    def __init__(self, state: State, create_epicycle_window: IWindow):
        self.state = state
        self.create_epicycle_window = create_epicycle_window

    def configure(self) -> Self:
        with dpg.window(tag=self.window_id, label="List Points", autosize=True):
            dpg.add_text("Points")

            dpg.add_button(label="Create point", callback=self.create_epicycle_window.show)

            # with dpg.group(horizontal=True):
            #     dpg.add_button(
            #         label="Update info",
            #         callback=lambda: menu_actions.update_figures_combobox(),
            #     )
            #     dpg.add_combo(
            #         [],
            #         label="Figure",
            #         tag="figure",
            #         callback=lambda: menu_actions.update_point_menu(),
            #     )
            # dpg.add_button(label="Update point", callback=show_update_point_modal)
            # dpg.add_button(
            #     label="Delete parent point",
            #     callback=lambda: object_actions.delete_point_callback(object_actions.get_point()),
            # )

            # dpg.add_listbox(
            #     [],
            #     label="children",
            #     tag="child",
            #     callback=lambda: menu_actions.update_modal_update_child(),
            # )
            # dpg.add_button(label="Add child", callback=show_create_child_modal)
            # dpg.add_button(label="Update child", callback=show_update_child_modal)
            # dpg.add_button(
            #     label="Delete child",
            #     callback=lambda: object_actions.delete_child_callback(
            #         object_actions.get_point(),
            #         object_actions.get_child_point(),
            #     ),
            # )

            # dpg.add_checkbox(label="Visible", tag="visible", enabled=False)
            # dpg.add_checkbox(label="Line", tag="line", enabled=False)
            # dpg.add_checkbox(label="Tracer", tag="tracer", enabled=False)
            # dpg.add_combo(
            #     config.Colors.get_colors(),
            #     label="Choose color",
            #     tag="color",
            #     default_value="WHITE",
            #     enabled=False,
            # )

            # dpg.add_slider_int(label="x", min_value=0, max_value=width, tag="x", enabled=False)
            # dpg.add_slider_int(label="y", min_value=0, max_value=height, tag="y", enabled=False)
            # dpg.add_slider_int(label="speed", min_value=-1000, max_value=1000, tag="speed", enabled=False)
            # dpg.add_slider_int(label="radius", min_value=1, max_value=1000, tag="radius", enabled=False)
            # dpg.add_slider_int(label="size", min_value=2, max_value=300, tag="size", enabled=False)

        self.hide()
        return self
