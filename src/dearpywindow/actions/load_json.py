from pathlib import Path

from epicycle import EpicycleWrapper, State
from epicycle.commands import DeleteAllWrappersCommand
from epicycle.config_loaders import JsonConfigLoader


def load_json_config(state: State):
    def _inner(_, app_data):
        file_path = Path(app_data["file_path_name"])
        epicycles = JsonConfigLoader(file_path).load()
        DeleteAllWrappersCommand(state).execute()
        wrapped_list = [EpicycleWrapper(epicycle) for epicycle in epicycles]
        state.wrappers = {wrapped.__hash__(): wrapped for wrapped in wrapped_list}

    return _inner
