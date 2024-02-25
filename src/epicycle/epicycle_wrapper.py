from math import cos, pi, sin

from .models import Epicycle, Point2D
from .types import ColorType


class EpicycleWrapper:
    """
    Wrapper for epicycle.

    Add logic for calculating new position, creating children

    Note: speed in minutes.
    """

    position: Point2D = Point2D(x=0, y=0)
    offset: float = 0
    epicycle: Epicycle

    def __init__(self, epicycle: Epicycle) -> None:
        self.epicycle = epicycle
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
    ):
        """Create new epicycle, then wrap it with EpicycleWrapper."""
        epicycle = Epicycle(
            center=center,
            speed=cls._minutes_to_radians(speed),
            radius=radius,
            size=size,
            color=color,
            visible=visible,
            has_connect_line=has_connect_line,
            has_tracer=has_tracer,
        )
        return cls(epicycle)

    def calculate_next_position(self):
        """Calculate next point position, then update all connected points."""
        x = cos(self.offset) * self.epicycle.radius + self.epicycle.center.x
        y = sin(self.offset) * self.epicycle.radius + self.epicycle.center.y
        self._get_new_offset()
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
    ) -> Epicycle:
        """
        Create child for this epicycle.

        Child inherits current parent position as center.
        """
        child = Epicycle(
            center=self.position,
            speed=speed,
            radius=radius,
            size=size,
            color=color,
            visible=visible,
            has_connect_line=has_connect_line,
            has_tracer=has_tracer,
        )
        self.epicycle.children.append(child)
        return child

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

    @staticmethod
    def _minutes_to_radians(minutes: int) -> float:
        return 2 * pi * minutes / (360 * 60)

    def _get_new_offset(self):
        self.offset += self.epicycle.speed
        if self.offset >= 2 * pi:
            self.offset -= 2 * pi

    def _calculate_connected_points(self):
        for child in self.epicycle.children:
            child.center = self.position
