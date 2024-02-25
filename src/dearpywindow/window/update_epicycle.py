from enum import Enum
from typing import Self

import dearpygui.dearpygui as dpg
from epicycle import Point2D, State
from type_alias import ColorType

from dearpywindow import actions
from dearpywindow.enums import WindowId

from .base import BaseWindow


class EpicycleUpdateEnum(str, Enum):
    visible = "update_visible"
    tracer = "update_tracer"
    connection_line = "update_connection_line"
    color = "update_color"
    x = "update_x"
    y = "update_y"
    speed = "update_speed"
    radius = "update_radius"
    size = "update_size"


class UpdateEpicycleWindow(BaseWindow):
    window_id = WindowId.update_epicycle

    def __init__(self, state: State, max_width: int, max_height: int):
        self.state = state
        self.max_width = max_width
        self.max_height = max_height
        self.no_wrapper_selected_window = NoWrapperSelectedErrorWindow().configure()

    def configure(self) -> Self:
        with dpg.window(
            modal=True,
            tag=self.window_id,
            label="Update Point",
        ):
            dpg.add_text(default_value="Point update")

            dpg.add_checkbox(label="Visible", tag=EpicycleUpdateEnum.visible, default_value=True)
            dpg.add_checkbox(label="Line", tag=EpicycleUpdateEnum.connection_line, default_value=True)
            dpg.add_checkbox(label="Tracer", tag=EpicycleUpdateEnum.tracer, default_value=True)
            dpg.add_color_picker(label="Epicycle color", tag=EpicycleUpdateEnum.color)

            dpg.add_slider_int(label="x", min_value=0, max_value=self.max_width, tag=EpicycleUpdateEnum.x)
            dpg.add_slider_int(label="y", min_value=0, max_value=self.max_height, tag=EpicycleUpdateEnum.y)
            dpg.add_slider_int(label="speed", min_value=-1000, max_value=1000, tag=EpicycleUpdateEnum.speed)
            dpg.add_slider_int(label="radius", min_value=1, max_value=1000, tag=EpicycleUpdateEnum.radius)
            dpg.add_slider_int(label="size", min_value=1, max_value=300, tag=EpicycleUpdateEnum.size, default_value=1)

            dpg.add_button(label="Create", callback=self._update_epicycle_handler)

        self.hide()
        return self

    def _update_values(self) -> None:
        selected_wrapper_id = self.state.selected_wrapper
        if not selected_wrapper_id:
            self.hide()
            self.no_wrapper_selected_window.show()
            return
        selected_wrapper = self.state.wrappers[selected_wrapper_id]
        dpg.set_value(EpicycleUpdateEnum.visible, selected_wrapper.epicycle.visible)
        dpg.set_value(EpicycleUpdateEnum.tracer, selected_wrapper.epicycle.has_tracer)
        dpg.set_value(EpicycleUpdateEnum.speed, selected_wrapper.get_speed())
        dpg.set_value(EpicycleUpdateEnum.connection_line, selected_wrapper.epicycle.has_connect_line)
        dpg.set_value(EpicycleUpdateEnum.radius, selected_wrapper.epicycle.radius)
        dpg.set_value(EpicycleUpdateEnum.size, selected_wrapper.epicycle.size)
        dpg.set_value(EpicycleUpdateEnum.color, selected_wrapper.epicycle.color)
        dpg.set_value(EpicycleUpdateEnum.x, selected_wrapper.epicycle.center.x)
        dpg.set_value(EpicycleUpdateEnum.y, selected_wrapper.epicycle.center.y)

    def _update_epicycle_handler(self) -> None:
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

        x = dpg.get_value(EpicycleUpdateEnum.x)
        y = dpg.get_value(EpicycleUpdateEnum.y)
        speed = dpg.get_value(EpicycleUpdateEnum.speed)
        radius = dpg.get_value(EpicycleUpdateEnum.radius)
        size = dpg.get_value(EpicycleUpdateEnum.size)

        actions.update_epicycle(
            wrapper=wrapper,
            center=Point2D(x=x, y=y),
            speed=speed,
            radius=radius,
            size=size,
            color=_transform_color(color),
            visible=visible,
            has_connect_line=connection_line,
            has_tracer=tracer,
        )

    def show(self) -> None:
        super().show()
        self._update_values()


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
