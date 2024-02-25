from pathlib import Path

from epicycle import EpicycleWrapper, State
from epicycle.commands import DeleteAllWrappersCommand
from epicycle.config_loaders import JsonConfigLoader
from epicycle.models import Epicycle


def load_json_config(state: State):
    def _inner(_, app_data):
        def _add_to_state(epicycle_list: list[Epicycle]):
            for epicycle in epicycle_list:
                _add_to_state(epicycle.children)
                wrapped = EpicycleWrapper(epicycle)
                state.wrappers[wrapped.__hash__()] = wrapped

        file_path = Path(app_data["file_path_name"])
        epicycles = JsonConfigLoader(file_path).load()
        DeleteAllWrappersCommand(state).execute()
        _add_to_state(epicycles)

    return _inner
