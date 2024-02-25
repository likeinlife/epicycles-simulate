from epicycle import EpicycleWrapper, Point2D, State
from type_alias import ColorType


def create_epicycle(
    state: State,
    center: Point2D,
    speed: int,
    radius: int,
    size: int,
    color: ColorType,
    visible: bool = True,
    has_connect_line: bool = True,
    has_tracer: bool = True,
) -> EpicycleWrapper:
    wrapper = EpicycleWrapper.new(
        center=center,
        speed=speed,
        radius=radius,
        size=size,
        color=color,
        visible=visible,
        has_connect_line=has_connect_line,
        has_tracer=has_tracer,
    )
    state.wrappers[wrapper.__hash__()] = wrapper
    return wrapper
