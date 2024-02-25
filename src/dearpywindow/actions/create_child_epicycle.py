from epicycle import EpicycleWrapper, State
from type_alias import ColorType


def create_child_epicycle(
    wrapper: EpicycleWrapper,
    state: State,
    speed: int,
    radius: int,
    size: int,
    color: ColorType,
    visible: bool = True,
    has_connect_line: bool = True,
    has_tracer: bool = True,
) -> EpicycleWrapper:
    child = wrapper.create_child(
        speed=speed,
        radius=radius,
        size=size,
        color=color,
        visible=visible,
        has_connect_line=has_connect_line,
        has_tracer=has_tracer,
    )
    state.wrappers[child.__hash__()] = child
    return child
