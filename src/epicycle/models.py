from __future__ import annotations

from pydantic import BaseModel, Field

from .types import ColorType


class Point2D(BaseModel):
    x: float
    y: float


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
