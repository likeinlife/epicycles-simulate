import dearpygui.dearpygui as dpg


def load_json_config(dpg_id: str):
    path = dpg.get_value(dpg_id)
    print(path)
