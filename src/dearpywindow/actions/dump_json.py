from pathlib import Path

from epicycle import State
from epicycle.config_dumpers import JsonConfigDumper


def dump_json_config(state: State):
    def _inner(_, app_data):
        file_path = Path(app_data["file_path_name"])
        print(file_path)
        epicycle_list = [wrapped.epicycle for wrapped in state.wrappers.values()]
        JsonConfigDumper(epicycle_list, file_path).dump()

    return _inner
