import dearpygui.dearpygui as dpg

from epicycle import config, point


def create_point():
    visible = dpg.get_value('visible')
    line = dpg.get_value('line')
    tracer = dpg.get_value('tracer')
    radius = dpg.get_value('radius')
    color = dpg.get_value('color')
    size = dpg.get_value('size')
    color_rgb = config.Colors.get_color(color)

    x = dpg.get_value('x')
    y = dpg.get_value('y')
    speed = dpg.get_value('speed')

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


def update_point(figure):

    figure.visible = dpg.get_value('visible')
    figure.need_to_draw_connecting_line = dpg.get_value('line')
    figure.need_to_draw_tracer = dpg.get_value('tracer')
    figure.radius = dpg.get_value('radius')
    color = dpg.get_value('color')
    figure.size = dpg.get_value('size')

    figure.color = config.Colors.get_color(color)

    figure.center = point.Point2D(dpg.get_value('x'), dpg.get_value('y'))
    figure.set_speed(dpg.get_value('speed'))


def pause():
    from epicycle import window
    window.pause = not window.pause


def clear_tracers():
    from epicycle import window
    window.clear_tracers()


def del_object():
    pass


def add_child(figure):

    visible = dpg.get_value('visible')
    line = dpg.get_value('line')
    tracer = dpg.get_value('tracer')
    radius = dpg.get_value('radius')
    color = dpg.get_value('color')
    size = dpg.get_value('size')
    color_rgb = config.Colors.get_color(color)

    speed = dpg.get_value('speed')

    p = figure.create_connected_point(
        speed,
        radius,
        size,
        color_rgb,
        visible,
        line,
        tracer,
    )
    dpg.set_value('figure', p)
