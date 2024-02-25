from __future__ import annotations

from pydantic import BaseModel, Field
from type_alias import ColorType


class Point2D(BaseModel):
    x: float
    y: float

    def to_tuple(self) -> tuple[float, float]:
        return self.x, self.y


class Epicycle(BaseModel):
    center: Point2D
    speed: float
    radius: int
    size: int
    color: ColorType
    visible: bool
    has_tracer: bool
    has_connect_line: bool

    children: list[Epicycle] = Field(default_factory=list)
