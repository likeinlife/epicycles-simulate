import dearpygui.dearpygui as dpg
from typing_extensions import assert_never

from epicycle import config, point

from . import functions
from .mode import Mode


def create_point_menu():
    dpg.configure_item('confirm', label='Create')
    dpg.set_value('figure', 'CREATION')
    dpg.set_value('mode', Mode.CREATE.value)


def confirm_action(figures: type[point.PointCounterMeta]):
    match dpg.get_value('mode'):
        case Mode.CREATE.value:
            functions.create_point()
        case Mode.UPDATE.value:
            functions.update_point(figures)
        case _ as element:
            assert_never(element)

    update_point_menu(figures)


def update_point_menu(figures: type[point.PointCounterMeta]):
    dpg.configure_item('confirm', label='Update')
    dpg.set_value('mode', Mode.UPDATE.value)
    figure: point.Point = figures.points_list[dpg.get_value('figure')]
    [figure.disable_selection() for figure in figures.points_list.values()]
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


def update_figures_combobox(figures_list: type[point.PointCounterMeta]):
    dpg.configure_item('figure', items=list(figures_list.points_list.keys()))


def set_values():
    with dpg.value_registry():
        dpg.add_int_value(tag='mode', default_value=Mode.CREATE.value)

def clear_selection(figures: type[point.PointCounterMeta]):
    [figure.disable_selection() for figure in figures.points_list.values()]


def main_window(figures: type[point.PointCounterMeta], WINDOW_HEIGHT: int, WINDOW_WIDTH: int,
                 colors: type[config.Colors]):
    with dpg.window(label="Figure setting", width=600, height=400, no_resize=True):
        dpg.add_button(
            label='New item',
            callback=create_point_menu,
        )
        dpg.add_button(
            label='Clear selection',
            callback=lambda: clear_selection(figures),
        )

        with dpg.group(horizontal=True):
            dpg.add_button(label='Update info', callback=lambda: update_figures_combobox(figures))
            dpg.add_combo(
                [],
                label='Figure',
                tag='figure',
                callback=lambda: update_point_menu(figures),
            )

        with dpg.group(horizontal=True):
            dpg.add_button(label='Clear objects', callback=functions.del_object)
            dpg.add_button(label='||', callback=functions.pause)
            dpg.add_button(label='Clear tracers', callback=functions.clear_tracers)


def edit_point_window(figure: point.Point, WINDOW_HEIGHT: int, WINDOW_WIDTH: int,
                 colors: type[config.Colors],):
    with dpg.popup(parent=dpg.last_item()):
        dpg.add_text(figure)

        dpg.add_checkbox(label="Visible", tag='visible')
        dpg.add_checkbox(label="Line", tag='line')
        dpg.add_checkbox(label="Tracer", tag='tracer')
        dpg.add_combo(colors.get_colors(), label='Choose color', tag='color', default_value='WHITE')

        dpg.add_slider_int(label="x", min_value=0, max_value=WINDOW_WIDTH, tag='x')
        dpg.add_slider_int(label="y", min_value=0, max_value=WINDOW_HEIGHT, tag='y')
        dpg.add_slider_int(label="speed", min_value=-1000, max_value=1000, tag='speed')
        dpg.add_slider_int(label="radius", min_value=0, max_value=1000, tag='radius')
        dpg.add_slider_int(label="size", min_value=0, max_value=1000, tag='size')

        dpg.add_listbox(figure.connected_points, label='Children')

        dpg.add_button(label='Update', tag='update', callback=lambda: functions.update_point(figure))
        dpg.add_button(label='Add child', tag='add_child')


def add_child_window(figure: point.Point, colors: type[config.Colors],):
    with dpg.popup(parent=dpg.last_item(), modal=True):
        dpg.add_text(f'{figure} > adding child')

        dpg.add_checkbox(label="Visible", tag='visible', default_value=True)
        dpg.add_checkbox(label="Line", tag='line', default_value=True)
        dpg.add_checkbox(label="Tracer", tag='tracer', default_value=True)
        dpg.add_combo(colors.get_colors(), label='Choose color', tag='color', default_value='WHITE')

        dpg.add_slider_int(label="speed", min_value=-1000, max_value=1000, tag='speed')
        dpg.add_slider_int(label="radius", min_value=0, max_value=1000, tag='radius')
        dpg.add_slider_int(label="size", min_value=0, max_value=1000, tag='size')

        dpg.add_listbox(figure.connected_points, label='Children')

        dpg.add_button(label='Create', tag='create_child', callback=lambda: functions.add_child(figure))

def main(
    figures: type[point.PointCounterMeta],
    WINDOW_HEIGHT: int,
    WINDOW_WIDTH: int,
    colors: type[config.Colors],
):
    dpg.create_context()
    dpg.create_viewport(width=600, height=400, resizable=False)
    dpg.setup_dearpygui()


    set_values()
    main_window(figures, WINDOW_HEIGHT, WINDOW_WIDTH, colors)

    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()