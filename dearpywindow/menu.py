import dearpygui.dearpygui as dpg

from epicycle import point

from .error import error_popup
from .menu_actions import set_values
from .windows import (
    create_modal_create_child,
    create_modal_create_point,
    create_modal_list_points,
    create_modal_update_child,
    create_modal_update_point,
    main_window,
)


def main(
    figures: type[point.PointCounterMeta],
    /,
    PYGAME_WINDOW_HEIGHT: int = 900,
    PYGAME_WINDOW_WIDTH: int = 1600,
    PGUI_HEIGHT: int = 400,
    PGUI_WIDTH: int = 700,
):
    dpg.create_context()
    dpg.create_viewport(width=PGUI_WIDTH, height=PGUI_HEIGHT, resizable=False)
    dpg.setup_dearpygui()

    set_values()
    main_window(figures)
    dpg.set_primary_window("main_window", True)
    create_modal_list_points(PYGAME_WINDOW_WIDTH, PYGAME_WINDOW_HEIGHT)
    create_modal_create_point(PYGAME_WINDOW_WIDTH, PYGAME_WINDOW_HEIGHT)
    create_modal_update_point(PYGAME_WINDOW_WIDTH, PYGAME_WINDOW_HEIGHT)

    create_modal_update_child(PYGAME_WINDOW_WIDTH, PYGAME_WINDOW_HEIGHT)
    create_modal_create_child(PYGAME_WINDOW_WIDTH, PYGAME_WINDOW_HEIGHT)

    error_popup("")

    dpg.set_viewport_always_top(True)

    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()
