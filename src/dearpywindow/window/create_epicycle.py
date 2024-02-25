from enum import Enum
from typing import Self

import dearpygui.dearpygui as dpg
from epicycle import Point2D, State
from type_alias import ColorType

from dearpywindow import actions
from dearpywindow.enums import WindowId

from .base import BaseWindow


class EpicycleCreateEnum(str, Enum):
    visible = "create_visible"
    tracer = "create_tracer"
    connection_line = "create_connection_line"
    color = "create_color"
    x = "create_x"
    y = "create_y"
    speed = "create_speed"
    radius = "create_radius"
    size = "create_size"


class CreateEpicycleWindow(BaseWindow):
    window_id = WindowId.create_epicycle

    def __init__(self, state: State, max_width: int, max_height: int):
        self.state = state
        self.max_width = max_width
        self.max_height = max_height

    def configure(self) -> Self:
        with dpg.window(
            modal=True,
            tag=self.window_id,
            label="Create Point",
            no_open_over_existing_popup=False,
        ):
            dpg.add_text(default_value="Point creation")

            dpg.add_checkbox(label="Visible", tag=EpicycleCreateEnum.visible, default_value=True)
            dpg.add_checkbox(label="Line", tag=EpicycleCreateEnum.connection_line, default_value=True)
            dpg.add_checkbox(label="Tracer", tag=EpicycleCreateEnum.tracer, default_value=True)
            dpg.add_color_picker(label="Epicycle color", tag=EpicycleCreateEnum.color)

            dpg.add_slider_int(label="x", min_value=0, max_value=self.max_width, tag=EpicycleCreateEnum.x)
            dpg.add_slider_int(label="y", min_value=0, max_value=self.max_height, tag=EpicycleCreateEnum.y)
            dpg.add_slider_int(label="speed", min_value=-1000, max_value=1000, tag=EpicycleCreateEnum.speed)
            dpg.add_slider_int(label="radius", min_value=1, max_value=1000, tag=EpicycleCreateEnum.radius)
            dpg.add_slider_int(label="size", min_value=1, max_value=300, tag=EpicycleCreateEnum.size, default_value=1)

            dpg.add_button(label="Create", callback=self._create_epicycle_handler)

        self.hide()
        return self

    def _create_epicycle_handler(self) -> None:
        def _transform_color(color: tuple[float, float, float, float]) -> ColorType:
            return (int(color[0]), int(color[1]), int(color[2]), int(color[3]))

        visible = dpg.get_value(EpicycleCreateEnum.visible)
        connection_line = dpg.get_value(EpicycleCreateEnum.connection_line)
        tracer = dpg.get_value(EpicycleCreateEnum.tracer)
        color = dpg.get_value(EpicycleCreateEnum.color)

        x = dpg.get_value(EpicycleCreateEnum.x)
        y = dpg.get_value(EpicycleCreateEnum.y)
        speed = dpg.get_value(EpicycleCreateEnum.speed)
        radius = dpg.get_value(EpicycleCreateEnum.radius)
        size = dpg.get_value(EpicycleCreateEnum.size)

        actions.create_epicycle(
            state=self.state,
            center=Point2D(x=x, y=y),
            speed=speed,
            radius=radius,
            size=size,
            color=_transform_color(color),
            visible=visible,
            has_connect_line=connection_line,
            has_tracer=tracer,
        )
