import dearpygui.dearpygui as dpg

from epicycle import point

from . import object_actions
from .mode import Mode
from .windows import *


def update_point_menu():
    """Update menus according to selected of created point"""
    figure = object_actions.get_point()
    [figure.disable_selection() for figure in point.PointCounterMeta.points_list.values()]
    figure.enable_selection()

    dpg.set_value('visible', figure.visible)
    dpg.set_value('tracer', figure.need_to_draw_tracer)
    dpg.set_value('line', figure.need_to_draw_connecting_line)
    dpg.set_value('color', figure.get_color())

    dpg.set_value('x', int(figure.center.x))
    dpg.set_value('y', int(figure.center.y))
    dpg.set_value('speed', figure.get_speed())
    dpg.set_value('radius', figure.radius)
    dpg.set_value('size', figure.size)

    #update child listbox
    dpg.configure_item('child', items=figure.connected_points)


def update_modal_update_point():
    """Updates widgets for selected point to update"""
    figure = object_actions.get_point()
    [figure.disable_selection() for figure in point.PointCounterMeta.points_list.values()]
    figure.enable_selection()

    dpg.set_value('update_visible', figure.visible)
    dpg.set_value('update_tracer', figure.need_to_draw_tracer)
    dpg.set_value('update_line', figure.need_to_draw_connecting_line)
    dpg.set_value('update_color', figure.get_color())

    dpg.set_value('update_x', int(figure.center.x))
    dpg.set_value('update_y', int(figure.center.y))
    dpg.set_value('update_speed', figure.get_speed())
    dpg.set_value('update_radius', figure.radius)
    dpg.set_value('update_size', figure.size)

    #update child listbox
    dpg.configure_item('child', items=figure.connected_points)


def update_modal_update_child():
    """Updates widgets for selected point to update"""
    figure = object_actions.get_child_point()
    [figure.disable_selection() for figure in point.PointCounterMeta.points_list.values()]
    figure.enable_selection()

    dpg.set_value('update_child_visible', figure.visible)
    dpg.set_value('update_child_tracer', figure.need_to_draw_tracer)
    dpg.set_value('update_child_line', figure.need_to_draw_connecting_line)
    dpg.set_value('update_child_color', figure.get_color())

    dpg.set_value('update_child_speed', figure.get_speed())
    dpg.set_value('update_child_radius', figure.radius)
    dpg.set_value('update_child_size', figure.size)


def update_figures_combobox():
    dpg.configure_item('figure', items=list(point.PointCounterMeta.points_list.keys()))


def set_values():
    with dpg.value_registry():
        dpg.add_int_value(tag='mode', default_value=Mode.CREATE.value)


def clear_selection(figures: type[point.PointCounterMeta]):
    [figure.disable_selection() for figure in figures.points_list.values()]