from __future__ import annotations
from math import pi, sin, cos
from typing import Any
from typing_extensions import Self


class Point2D:

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    @property
    def coordinates(self) -> tuple[float, float]:
        return self.x, self.y

    def __repr__(self) -> str:
        return f'x = {self.x}, y = {self.y}'


class PointCounterMeta(type):

    points_list: list[Point] = []

    def __call__(cls, *args: Any, **kwds: Any) -> Any:
        instance = super().__call__(*args, **kwds)
        cls.points_list.append(instance)
        return instance


class Point(metaclass=PointCounterMeta):

    def __init__(self, center: Point2D, speed: int, radius: int, size: int, color: tuple[int, int, int]) -> None:
        """
        Args:
            center (tuple[int, int]): center coordinates: x, y
            speed (int): speed in minutes. shows how much point goes in one frame
            radius (int): radius of circle
        """
        self.center: Point2D = center
        self.speed: float = self.__minutes_to_radians(speed)
        self.radius: int = radius
        self.size: int = size
        self.color: tuple[int, int, int] = color
        self.connected_points: list[Point] = []
        self.offset = 0
        self.point = self.calculate_next_point_pos()

    def calculate_next_point_pos(self):
        x = cos(self.offset) * self.radius + self.center.x
        y = sin(self.offset) * self.radius + self.center.y
        self.__get_new_offset()
        point = Point2D(x, y)
        self.point = point
        self.__calculate_connected_points()
        return point

    def create_connected_point(self, speed: int, radius: int, size: int, color: tuple[int, int, int]) -> Point:
        another_point = Point(self.point, speed, radius, size, color)
        self.connected_points.append(another_point)
        return another_point

    def __calculate_connected_points(self):
        for point in self.connected_points:
            point.center = self.point

    def __get_new_offset(self):
        self.offset += self.speed
        if self.offset >= 2 * pi:
            self.offset -= 2 * pi

    @staticmethod
    def __minutes_to_radians(minutes: int) -> float:
        return 2 * pi * minutes / (360 * 60)
