from __future__ import annotations

from math import cos, pi, sin

from type_alias import ColorType

from .models import Epicycle, Point2D


class EpicycleWrapper:
    """
    Wrapper for epicycle.

    Add logic for calculating new position, creating children

    Note: speed in minutes.
    """

    position: Point2D
    offset: float
    epicycle: Epicycle
    wrapper_set: set[EpicycleWrapper] = set()

    def __init__(self, epicycle: Epicycle) -> None:
        self.epicycle = epicycle
        self.position = Point2D(x=epicycle.center.x, y=epicycle.center.y + epicycle.radius)
        self.offset = 0
        self.children: list[EpicycleWrapper] = []
        self.calculate_next_position()

    @classmethod
    def new(
        cls,
        center: Point2D,
        speed: int,
        radius: int,
        size: int,
        color: ColorType,
        visible: bool = True,
        has_connect_line: bool = True,
        has_tracer: bool = True,
        *,
        is_parent: bool = True,
    ) -> EpicycleWrapper:
        """
        Create new epicycle, then wrap it with EpicycleWrapper.

        Add all created objects to wrapper_list.
        """
        epicycle = Epicycle(
            is_parent=is_parent,
            center=center,
            speed=cls._minutes_to_radians(speed),
            radius=radius,
            size=size,
            color=color,
            visible=visible,
            has_connect_line=has_connect_line,
            has_tracer=has_tracer,
        )
        wrapper = cls(epicycle)
        cls.wrapper_set.add(wrapper)
        return wrapper

    def calculate_next_position(self):
        """Calculate next point position, then update all connected points."""
        x = cos(self.offset) * self.epicycle.radius + self.epicycle.center.x
        y = sin(self.offset) * self.epicycle.radius + self.epicycle.center.y
        self._update_offset()
        self.position.x = x
        self.position.y = y
        self._calculate_connected_points()

    def create_child(
        self,
        speed: int,
        radius: int,
        size: int,
        color: ColorType,
        visible: bool = True,
        has_connect_line: bool = True,
        has_tracer: bool = True,
    ) -> EpicycleWrapper:
        """
        Create child for this epicycle.

        Child inherits current parent position as center.
        """
        child_wrapper = self.new(
            center=self.position.model_copy(),
            speed=speed,
            radius=radius,
            size=size,
            color=color,
            visible=visible,
            has_connect_line=has_connect_line,
            has_tracer=has_tracer,
            is_parent=False,
        )
        self.epicycle.children.append(child_wrapper.epicycle)
        self.children.append(child_wrapper)
        return child_wrapper

    def update(
        self,
        *,
        center: Point2D | None = None,
        radius: int | None = None,
        size: int | None = None,
        color: ColorType | None,
        speed: int | None = None,
        visible: bool | None = None,
        has_tracer: bool | None = None,
        has_connect_line: bool | None = None,
    ):
        """
        Update epicycle properties.

        Note: speed in minutes.
        """
        if center:
            self.epicycle.center = center
        if radius:
            self.epicycle.radius = radius
        if size:
            self.epicycle.size = size
        if color:
            self.epicycle.color = color
        if speed:
            self.epicycle.speed = self._minutes_to_radians(speed)
        if visible:
            self.epicycle.visible = visible
        if has_tracer:
            self.epicycle.has_tracer = has_tracer
        if has_connect_line:
            self.epicycle.has_connect_line = has_connect_line

    def get_speed(self) -> int:
        return int(360 * 60 * self.epicycle.speed / (2 * pi))

    @staticmethod
    def _minutes_to_radians(minutes: int) -> float:
        return 2 * pi * minutes / (360 * 60)

    def _update_offset(self):
        self.offset += self.epicycle.speed
        if self.offset >= 2 * pi:
            self.offset -= 2 * pi

    def _calculate_connected_points(self):
        for child in self.epicycle.children:
            child.center.x = self.position.x
            child.center.y = self.position.y
