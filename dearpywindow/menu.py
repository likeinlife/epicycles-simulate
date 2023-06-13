import dearpygui.dearpygui as dpg

from epicycle import config, point

from .error import error_popup
from .menu_actions import set_values
from .windows import (create_modal_create_child, create_modal_create_point, create_modal_list_points,
                      create_modal_update_child, create_modal_update_point, main_window)


def main(
    figures: type[point.PointCounterMeta],
    WINDOW_HEIGHT: int,
    WINDOW_WIDTH: int,
):
    dpg.create_context()
    dpg.create_viewport(width=500, height=600, resizable=False)
    dpg.setup_dearpygui()

    set_values()
    main_window(figures, WINDOW_HEIGHT, WINDOW_WIDTH)
    create_modal_list_points(WINDOW_WIDTH, WINDOW_HEIGHT)
    create_modal_create_point(WINDOW_WIDTH, WINDOW_HEIGHT)
    create_modal_update_point(WINDOW_WIDTH, WINDOW_HEIGHT)

    create_modal_update_child(WINDOW_WIDTH, WINDOW_HEIGHT)
    create_modal_create_child(WINDOW_WIDTH, WINDOW_HEIGHT)

    error_popup('')

    dpg.set_viewport_always_top(True)

    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()