from .config import Colors, Config
from .point import Point, Point2D

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
