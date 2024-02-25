from enum import Enum
from typing import Self

import dearpygui.dearpygui as dpg
from epicycle import State
from type_alias import ColorType

from dearpywindow import actions
from dearpywindow.enums import WindowId

from .base import BaseWindow
from .interface import IWindow


class EpicycleUpdateEnum(str, Enum):
    visible = "create_child_visible"
    tracer = "create_child_tracer"
    connection_line = "create_child_connection_line"
    color = "create_child_color"
    x = "create_child_x"
    y = "create_child_y"
    speed = "create_child_speed"
    radius = "create_child_radius"
    size = "create_child_size"


class CreateChildEpicycleWindow(BaseWindow):
    window_id = WindowId.create_child_epicycle

    def __init__(
        self,
        state: State,
        max_width: int,
        max_height: int,
        no_wrapper_selected_window: IWindow,
    ):
        self.state = state
        self.max_width = max_width
        self.max_height = max_height
        self.no_wrapper_selected_window = no_wrapper_selected_window

    def configure(self) -> Self:
        with dpg.window(
            modal=True,
            tag=self.window_id,
            label="Create child epicycle",
        ):
            dpg.add_text(default_value="Create child epicycle")

            dpg.add_checkbox(label="Visible", tag=EpicycleUpdateEnum.visible, default_value=True)
            dpg.add_checkbox(label="Line", tag=EpicycleUpdateEnum.connection_line, default_value=True)
            dpg.add_checkbox(label="Tracer", tag=EpicycleUpdateEnum.tracer, default_value=True)
            dpg.add_color_picker(label="Epicycle color", tag=EpicycleUpdateEnum.color)

            dpg.add_slider_int(label="speed", min_value=-1000, max_value=1000, tag=EpicycleUpdateEnum.speed)
            dpg.add_slider_int(label="radius", min_value=1, max_value=1000, tag=EpicycleUpdateEnum.radius)
            dpg.add_slider_int(label="size", min_value=1, max_value=300, tag=EpicycleUpdateEnum.size, default_value=1)

            dpg.add_button(label="Create child", callback=self._create_child_handler)

        self.hide()
        return self

    def _create_child_handler(self) -> None:
        def _transform_color(color: tuple[float, float, float, float]) -> ColorType:
            return (int(color[0]), int(color[1]), int(color[2]), int(color[3]))

        wrapper_id = self.state.selected_wrapper
        if not wrapper_id:
            self.hide()
            self.no_wrapper_selected_window.show()
            return

        wrapper = self.state.wrappers[wrapper_id]

        visible = dpg.get_value(EpicycleUpdateEnum.visible)
        connection_line = dpg.get_value(EpicycleUpdateEnum.connection_line)
        tracer = dpg.get_value(EpicycleUpdateEnum.tracer)
        color = dpg.get_value(EpicycleUpdateEnum.color)

        speed = dpg.get_value(EpicycleUpdateEnum.speed)
        radius = dpg.get_value(EpicycleUpdateEnum.radius)
        size = dpg.get_value(EpicycleUpdateEnum.size)

        actions.create_child_epicycle(
            wrapper=wrapper,
            state=self.state,
            speed=speed,
            radius=radius,
            size=size,
            color=_transform_color(color),
            visible=visible,
            has_connect_line=connection_line,
            has_tracer=tracer,
        )

    def show(self) -> None:
        wrapper_id = self.state.selected_wrapper
        if not wrapper_id:
            self.hide()
            self.no_wrapper_selected_window.show()
        else:
            super().show()
