from epicycle.epicycle_wrapper import EpicycleWrapper
from epicycle.models import Point2D
from epicycle.state import State
from pygame_view.enums import Color


# TODO: Delete later
def create_points() -> State:
    point1 = EpicycleWrapper.new(Point2D(x=300, y=400), 200, 30, 10, Color.black)
    point2 = point1.create_child(100, 100, 5, Color.blue)
    point2.create_child(-20, 50, 5, Color.red)

    return State(wrapper_list=list(EpicycleWrapper.wrapper_set))

    # middle_point = EpicycleWrapper.new(Point2D(x=500, y=500), 140, 30, 30, Color.red)
    # mid_p_2 = middle_point.create_child(-200, 80, 20, Color.cyan, False, False, False)
    # mid_p_2.create_child(-160, 120, 5, Color.black)
