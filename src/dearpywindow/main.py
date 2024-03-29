import dearpygui.dearpygui as dpg
from epicycle.state import State

from . import window
from .protocols import PyGameWindow


def start(
    state: State,
    pygame_window: PyGameWindow,
    pygame_window_height: int,
    pygame_window_width: int,
    pgui_height: int = 1000,
    pgui_width: int = 800,
):
    dpg.create_context()
    dpg.create_viewport(width=pgui_width, height=pgui_height, resizable=True)
    dpg.setup_dearpygui()

    create_epicycle_window = window.CreateEpicycleWindow(
        state,
        pygame_window_width,
        pygame_window_height,
    ).configure()

    no_wrapper_selected_window = window.popups.NoWrapperSelectedErrorWindow().configure()
    update_epicycle_window = window.UpdateEpicycleWindow(
        state,
        pygame_window_width,
        pygame_window_height,
        no_wrapper_selected_window,
    ).configure()
    delete_epicycle_window = window.DeleteEpicycleWindow(
        state,
        no_wrapper_selected_window,
    ).configure()

    create_child_epicycle_window = window.CreateChildEpicycleWindow(
        state,
        pygame_window_width,
        pygame_window_height,
        no_wrapper_selected_window,
    ).configure()

    epicycles_menu = window.EpicyclesMenuWindow(
        state,
        create_epicycle_window,
        update_epicycle_window,
        delete_epicycle_window,
        create_child_epicycle_window,
    ).configure()

    main_window = window.MainWindow(
        state=state,
        epicycles_menu=epicycles_menu,
        pygame_window=pygame_window,
    ).configure()

    dpg.set_primary_window(main_window.window_id, True)

    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()
