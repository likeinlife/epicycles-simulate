from epicycle import EpicycleWrapper, Point2D
from type_alias import ColorType


def update_epicycle(
    wrapper: EpicycleWrapper,
    center: Point2D,
    speed: int,
    radius: int,
    size: int,
    color: ColorType,
    visible: bool = True,
    has_connect_line: bool = True,
    has_tracer: bool = True,
) -> EpicycleWrapper:
    wrapper.update(
        center=center,
        speed=speed,
        radius=radius,
        size=size,
        color=color,
        visible=visible,
        has_connect_line=has_connect_line,
        has_tracer=has_tracer,
    )

    return wrapper
