import json
from pathlib import Path

from pydantic import TypeAdapter

from window.models import Epicycle

from .interface import IConfigLoader


class JsonConfigLoader(IConfigLoader):
    """
    Parse json-doc to load Points.

    JSON document example:
    ```json
        [
            {
                "size": 10,
                "color": [0, 0, 0],
                "x": 10,
                "y": 200,
                "radius": 20,
                "speed": 100,
                "visible": true,
                "line": true,
                "tracer": true,
                "children": [],
            }
        ]
    ```
    """

    def __init__(self, json_path: Path) -> None:
        self.json_path = json_path

    def load(self) -> list[Epicycle]:
        loaded_json = self._load_file(self.json_path)
        adapted = TypeAdapter(list[Epicycle]).validate_python(loaded_json)
        return adapted

    def _load_file(self, json_path: Path) -> list[dict]:
        with open(json_path, "r") as file_obj:
            return json.load(file_obj)
