import dearpygui.dearpygui as dpg


def show_error(message: str):
    dpg.configure_item('message_error', default_value=message)
    dpg.show_item('error_popup')


def error_popup(message: str):
    with dpg.window(
            label='Error',
            autosize=True,
            tag='error_popup',
            no_move=True,
            no_collapse=True,
            popup=True,
            no_open_over_existing_popup=False,
    ):
        dpg.add_text(message, tag='message_error')
        dpg.add_button(label='Close', callback=lambda: dpg.hide_item('error_popup'))

    dpg.hide_item('error_popup')
