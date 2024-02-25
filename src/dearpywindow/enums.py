from enum import Enum, auto


class WindowId(int, Enum):
    main = auto()
    epicycles_menu = auto()
    create_epicycle = auto()
    update_epicycle = auto()
    no_wrapper_selected = auto()
