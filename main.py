import threading

import dearpywindow
from epicycle import __main__, config, point


def pg():
    __main__.main()


def pgui():
    dearpywindow.menu.main(
        point.PointCounterMeta,
        config.Config.SCREEN_HEIGHT,
        config.Config.SCREEN_WIDTH,
        config.Colors,
    )


if __name__ == '__main__':
    pg_thread = threading.Thread(target=pg)
    pgui_thread = threading.Thread(target=pgui)

    pgui_thread.start()
    pg_thread.start()
