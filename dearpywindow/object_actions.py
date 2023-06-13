import dearpygui.dearpygui as dpg

from dearpywindow import menu_actions
from epicycle import config, point

from . import error


def get_point() -> point.Point:
    if (sel_point := dpg.get_value('figure')):
        return point.PointCounterMeta.points_list[sel_point]
    else:
        error.show_error('No figure selected')
        raise IndexError('No figure selected')


def get_child_point() -> point.Point:
    if (sel_point := dpg.get_value('child')):
        return point.PointCounterMeta.points_list[sel_point]
    else:
        error.show_error('No child selected')
        raise IndexError('No child selected')


def create_point():
    visible = dpg.get_value('create_visible')
    line = dpg.get_value('create_line')
    tracer = dpg.get_value('create_tracer')
    radius = dpg.get_value('create_radius')
    color = dpg.get_value('create_color')
    size = dpg.get_value('create_size')
    color_rgb = config.Colors.get_color(color)

    x = dpg.get_value('create_x')
    y = dpg.get_value('create_y')
    speed = dpg.get_value('create_speed')

    p = point.Point(
        point.Point2D(x, y),
        speed,
        radius,
        size,
        color_rgb,
        visible,
        line,
        tracer,
    )
    dpg.set_value('figure', p)
    menu_actions.update_point_menu()
    dpg.hide_item('create_point_modal')


def update_point(figure: point.Point):

    figure.visible = dpg.get_value('update_visible')
    figure.need_to_draw_connecting_line = dpg.get_value('update_line')
    figure.need_to_draw_tracer = dpg.get_value('update_tracer')
    figure.radius = dpg.get_value('update_radius')
    color = dpg.get_value('update_color')
    figure.size = dpg.get_value('update_size')

    figure.color = config.Colors.get_color(color)

    figure.center = point.Point2D(dpg.get_value('update_x'), dpg.get_value('update_y'))
    figure.set_speed(dpg.get_value('update_speed'))


def pause():
    from epicycle import window
    window.pause = not window.pause


def clear_tracers():
    from epicycle import window
    window.clear_tracers()


def del_object():
    pass


def create_child(figure: point.Point):

    visible = dpg.get_value('create_child_visible')
    line = dpg.get_value('create_child_line')
    tracer = dpg.get_value('create_child_tracer')
    radius = dpg.get_value('create_child_radius')
    color = dpg.get_value('create_child_color')
    size = dpg.get_value('create_child_size')
    color_rgb = config.Colors.get_color(color)

    speed = dpg.get_value('create_child_speed')

    p = figure.create_connected_point(
        speed,
        radius,
        size,
        color_rgb,
        visible,
        line,
        tracer,
    )
    dpg.set_value('child', p)
    dpg.hide_item('create_child_modal')
    menu_actions.update_point_menu()


def update_child(figure: point.Point):

    figure.visible = dpg.get_value('update_child_visible')
    figure.need_to_draw_connecting_line = dpg.get_value('update_child_line')
    figure.need_to_draw_tracer = dpg.get_value('update_child_tracer')
    figure.radius = dpg.get_value('update_child_radius')
    color = dpg.get_value('update_child_color')
    figure.size = dpg.get_value('update_child_size')
    figure.color = config.Colors.get_color(color)

    figure.set_speed(dpg.get_value('update_child_speed'))
