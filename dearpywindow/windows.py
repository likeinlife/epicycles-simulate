import dearpygui.dearpygui as dpg

from epicycle import config, point

from . import menu_actions, object_actions


def main_window(
    figures: type[point.PointCounterMeta],
    WINDOW_HEIGHT: int,
    WINDOW_WIDTH: int,
):
    with dpg.window(label="Epicycles", tag='main_window'):
        dpg.add_button(
            label='Points',
            callback=show_list_point_modal,
        )
        dpg.add_button(
            label='Clear selection',
            callback=lambda: menu_actions.clear_selection(figures),
        )

        with dpg.group(horizontal=True):
            dpg.add_button(label='Clear objects', callback=object_actions.del_objects)
            dpg.add_button(label='||', callback=object_actions.pause)
            dpg.add_button(label='Clear tracers', callback=object_actions.clear_tracers)

        with dpg.file_dialog(
                label='Load Json config',
                show=False,
                directory_selector=False,
                callback=menu_actions.load_json_callback,
                cancel_callback=menu_actions.load_json_cancel_callback,
                tag='load_file',
                width=700,
                height=400,
        ):
            dpg.add_file_extension('.json', color=(70, 200, 70, 255))

        dpg.add_button(label='Load json config', callback=lambda: dpg.show_item('load_file'))

        with dpg.file_dialog(
                label='Dump config to json',
                show=False,
                directory_selector=False,
                callback=menu_actions.dump_json_callback,
                cancel_callback=menu_actions.dump_json_cancel_callback,
                tag='dump_file',
                width=700,
                height=400,
        ):
            dpg.add_file_extension('.json', color=(70, 200, 70, 255))

        dpg.add_button(label='Dump config to json', callback=lambda: dpg.show_item('dump_file'))


def show_create_point_modal():
    dpg.show_item('create_point_modal')


list_opened = False


def show_list_point_modal():
    global list_opened
    if list_opened:
        dpg.hide_item('list_points_modal')
    else:
        dpg.show_item('list_points_modal')
    list_opened = not list_opened


def show_update_point_modal():
    menu_actions.update_modal_update_point()
    dpg.show_item('update_point_modal')


def create_modal_list_points(width: int, height: int):
    """Create show current point info modal window"""
    with dpg.window(tag='list_points_modal', label='List Points', autosize=True):
        dpg.add_text(f'Points')

        dpg.add_button(label='Create point', callback=show_create_point_modal)

        with dpg.group(horizontal=True):
            dpg.add_button(
                label='Update info',
                callback=lambda: menu_actions.update_figures_combobox(),
            )
            dpg.add_combo(
                [],
                label='Figure',
                tag='figure',
                callback=lambda: menu_actions.update_point_menu(),
            )
        dpg.add_button(label='Update point', callback=show_update_point_modal)
        dpg.add_button(
            label='Delete parent point',
            callback=lambda: object_actions.delete_point_callback(object_actions.get_point()),
        )

        dpg.add_listbox(
            [],
            label='children',
            tag='child',
            callback=lambda: menu_actions.update_modal_update_child(),
        )
        dpg.add_button(label='Add child', callback=show_create_child_modal)
        dpg.add_button(label='Update child', callback=show_update_child_modal)
        dpg.add_button(
            label='Delete child',
            callback=lambda: object_actions.delete_child_callback(
                object_actions.get_point(),
                object_actions.get_child_point(),
            ),
        )

        dpg.add_checkbox(label="Visible", tag='visible', enabled=False)
        dpg.add_checkbox(label="Line", tag='line', enabled=False)
        dpg.add_checkbox(label="Tracer", tag='tracer', enabled=False)
        dpg.add_combo(config.Colors.get_colors(),
                      label='Choose color',
                      tag='color',
                      default_value='WHITE',
                      enabled=False)

        dpg.add_slider_int(label="x", min_value=0, max_value=width, tag='x', enabled=False)
        dpg.add_slider_int(label="y", min_value=0, max_value=height, tag='y', enabled=False)
        dpg.add_slider_int(label="speed", min_value=-1000, max_value=1000, tag='speed', enabled=False)
        dpg.add_slider_int(label="radius", min_value=1, max_value=1000, tag='radius', enabled=False)
        dpg.add_slider_int(label="size", min_value=2, max_value=300, tag='size', enabled=False)

    dpg.hide_item('list_points_modal')


def create_modal_create_point(width: int, height: int):
    """Create new point modal window"""
    with dpg.window(modal=True, tag='create_point_modal', label='Create Point', no_open_over_existing_popup=False):
        dpg.add_text(default_value='Point creation')

        dpg.add_checkbox(label="Visible", tag='create_visible')
        dpg.add_checkbox(label="Line", tag='create_line')
        dpg.add_checkbox(label="Tracer", tag='create_tracer')
        dpg.add_combo(config.Colors.get_colors(), label='Choose color', tag='create_color', default_value='WHITE')

        dpg.add_slider_int(label="x", min_value=0, max_value=width, tag='create_x')
        dpg.add_slider_int(label="y", min_value=0, max_value=height, tag='create_y')
        dpg.add_slider_int(label="speed", min_value=-1000, max_value=1000, tag='create_speed')
        dpg.add_slider_int(label="radius", min_value=1, max_value=1000, tag='create_radius')
        dpg.add_slider_int(label="size", min_value=1, max_value=300, tag='create_size', default_value=1)

        dpg.add_button(label='Create', callback=lambda: object_actions.create_point())

    dpg.hide_item('create_point_modal')


def create_modal_update_point(width: int, height: int):
    """Create update point model window"""
    with dpg.window(modal=True, tag='update_point_modal', label='UpdatePoint', no_open_over_existing_popup=False):
        dpg.add_text(f'{dpg.get_value("point")} update')

        dpg.add_checkbox(label="Visible", tag='update_visible')
        dpg.add_checkbox(label="Line", tag='update_line')
        dpg.add_checkbox(label="Tracer", tag='update_tracer')
        dpg.add_combo(config.Colors.get_colors(), label='Choose color', tag='update_color', default_value='WHITE')

        dpg.add_slider_int(label="x", min_value=0, max_value=width, tag='update_x')
        dpg.add_slider_int(label="y", min_value=0, max_value=height, tag='update_y')
        dpg.add_slider_int(label="speed", min_value=-1000, max_value=1000, tag='update_speed')
        dpg.add_slider_int(label="radius", min_value=1, max_value=1000, tag='update_radius')
        dpg.add_slider_int(label="size", min_value=1, max_value=300, tag='update_size', default_value=1)

        dpg.add_button(label='Update', callback=lambda: object_actions.update_point(object_actions.get_point()))

    dpg.hide_item('update_point_modal')


def show_create_child_modal():
    dpg.show_item('create_child_modal')


def show_update_child_modal():
    menu_actions.update_modal_update_child()
    dpg.show_item('update_child_modal')


def create_modal_create_child(width: int, height: int):
    """Create new child modal window"""
    with dpg.window(modal=True, tag='create_child_modal', label='Create Child', no_open_over_existing_popup=False):
        dpg.add_text(default_value='Child creation')

        dpg.add_checkbox(label="Visible", tag='create_child_visible')
        dpg.add_checkbox(label="Line", tag='create_child_line')
        dpg.add_checkbox(label="Tracer", tag='create_child_tracer')
        dpg.add_combo(config.Colors.get_colors(), label='Choose color', tag='create_child_color', default_value='WHITE')

        dpg.add_slider_int(label="speed", min_value=-1000, max_value=1000, tag='create_child_speed')
        dpg.add_slider_int(label="radius", min_value=1, max_value=1000, tag='create_child_radius')
        dpg.add_slider_int(label="size", min_value=1, max_value=300, tag='create_child_size', default_value=1)

        dpg.add_button(label='Create child', callback=lambda: object_actions.create_child(object_actions.get_point()))

    dpg.hide_item('create_child_modal')


def create_modal_update_child(width: int, height: int):
    """Update child modal window"""
    with dpg.window(modal=True, tag='update_child_modal', label='Update Child', no_open_over_existing_popup=False):
        dpg.add_text(default_value='Child update')

        dpg.add_checkbox(label="Visible", tag='update_child_visible')
        dpg.add_checkbox(label="Line", tag='update_child_line')
        dpg.add_checkbox(label="Tracer", tag='update_child_tracer')
        dpg.add_combo(config.Colors.get_colors(), label='Choose color', tag='update_child_color', default_value='WHITE')

        dpg.add_slider_int(label="speed", min_value=-1000, max_value=1000, tag='update_child_speed')
        dpg.add_slider_int(label="radius", min_value=1, max_value=1000, tag='update_child_radius')
        dpg.add_slider_int(label="size", min_value=1, max_value=300, tag='update_child_size', default_value=1)

        dpg.add_button(label='Update child',
                       callback=lambda: object_actions.update_child(object_actions.get_child_point()))

    dpg.hide_item('update_child_modal')