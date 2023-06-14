import json
from pathlib import Path

from .config import Colors, Config
from .point import Point, Point2D


def create_points():
    point1 = Point(Point2D(300, 400), 200, 30, 10, Colors.BLACK)
    point2 = point1.create_connected_point(100, 70, 5, Colors.BLUE)
    point2.create_connected_point(-20, 50, 5, Colors.RED)

    # point3 = Point(Point2D(200, 200), 100, 100, 40, Colors.GREEN)
    # point_4 = point3.create_connected_point(200, 150, 20, Colors.BLUE)

    # point_low_edge = Point(Point2D(Config.SCREEN_WIDTH - 50, Config.SCREEN_HEIGHT - 50), 100, 100, 40, Colors.GREEN)
    # point_low_edge.create_connected_point(100, 120, 30, Colors.MAGENTA)

    middle_point = Point(Point2D(Config.SCREEN_WIDTH // 2, Config.SCREEN_HEIGHT // 2), 140, 30, 30, Colors.RED)
    mid_p_2 = middle_point.create_connected_point(-200, 80, 20, Colors.CYAN, False, False, False)
    mid_p_2.create_connected_point(-160, 120, 5, Colors.BLACK)


class LoadPointsFromJSON:
    """Parse json-doc to load Points
    JSON doc example:
    [
    {
        "size": 10,
        "color": BLUE,
        "x": 10,
        "y": 200,
        "radius": 20,
        "speed": 100,
        "visible": true,
        "line": true,
        "tracer": true,
        "children": {

        },
        }
    ]"""

    def __init__(self, path_to_json: Path) -> None:
        self.path_to_json = path_to_json
        self.load()
        self.parse_json()

    def load(self):
        with open(self.path_to_json, 'r') as file_obj:
            self.json_config: list[dict] = json.load(file_obj)

    def parse_json(self):
        for point in self.json_config:
            size = point.get('size', 1)
            color = point.get('color', 'BLACK')

            color_RGB = Colors.get_color(color)
            x = point.get('x', 0)
            y = point.get('y', 0)
            radius = point.get('radius', 0)
            speed = point.get('speed', 0)
            visible = point.get('visible', 1)
            line = point.get('line', 1)
            tracer = point.get('tracer', 1)

            parent_point = Point(
                Point2D(x, y),
                speed,
                radius,
                size,
                color_RGB,
                visible,
                line,
                tracer,
            )

            if (children_list := point.get('children')) is not None:
                self.parse_children(parent_point, children_list)

    def parse_children(self, parent_point: Point, children_list: list[dict]):
        for child in children_list:
            size = child.get('size', 1)
            color = child.get('color', 'BLACk')

            color_RGB = Colors.get_color(color)
            radius = child.get('radius', 0)
            speed = child.get('speed', 0)
            visible = child.get('visible', 1)
            line = child.get('line', 1)
            tracer = child.get('tracer', 1)

            child_point = parent_point.create_connected_point(
                speed,
                radius,
                size,
                color_RGB,
                visible,
                line,
                tracer,
            )
            if (children_list := child.get('children')) is not None:  # type: ignore
                self.parse_children(child_point, children_list)


class DumpPointToJson:

    def __init__(self, points_list: list[Point], path_to_dump: Path) -> None:
        self.points_list = points_list
        self.path_to_dump = path_to_dump
        self.json_obj: list[dict] = []
        self.seen_object: list[Point] = []
        self._get_parents()
        self.dump()

    def dump(self):
        with open(self.path_to_dump, 'w') as file_obj:
            json.dump(self.json_obj, file_obj, indent=4, ensure_ascii=False)

    def _get_parents(self):
        for point in self.points_list:
            if point.is_parent:
                size = point.size
                color = point.get_color()

                x = point.center.x
                y = point.center.y
                radius = point.radius
                speed = point.get_speed()
                visible = point.visible
                line = point.need_to_draw_connecting_line
                tracer = point.need_to_draw_tracer

                point_dict = ({
                    "size": size,
                    "color": color,
                    "x": x,
                    "y": y,
                    "radius": radius,
                    "speed": speed,
                    "visible": visible,
                    "line": line,
                    "tracer": tracer,
                })

                if point.connected_points:
                    self._add_children(point_dict, point.connected_points)

                self.json_obj.append(point_dict)

    def _add_children(self, parent_point_dict: dict, children_list: list[Point]):
        for child in children_list:
            size = child.size
            color = child.get_color()

            radius = child.radius
            speed = child.get_speed()
            visible = child.visible
            line = child.need_to_draw_connecting_line
            tracer = child.need_to_draw_tracer

            child_point_dict = ({
                "size": size,
                "color": color,
                "radius": radius,
                "speed": speed,
                "visible": visible,
                "line": line,
                "tracer": tracer,
            })

            if child.connected_points:
                self._add_children(child_point_dict, child.connected_points)

            if parent_point_dict.get("children"):
                parent_point_dict["children"].append(child_point_dict)
            else:
                parent_point_dict["children"] = [child_point_dict]
