import json
from pathlib import Path

from epicycle.models import Epicycle


class JsonConfigDumper:
    def __init__(self, epicycle_list: list[Epicycle], json_path: Path) -> None:
        self.epicycle_list = epicycle_list
        self.json_path = json_path

    def dump(self):
        content = [epicycle.model_dump(mode="json") for epicycle in self.epicycle_list if epicycle.is_parent]
        with open(self.json_path, "w") as file_obj:
            json.dump(content, file_obj, indent=4, ensure_ascii=False)
