from enum import Enum, auto


class WindowId(int, Enum):
    main = auto()
    epicycles_menu = auto()
    create_epicycle = auto()
