import threading

import dearpywindow
from epicycle import __main__, config, point


def pg():
    __main__.main()


def pgui():
    dearpywindow.menu.main(
        point.PointCounterMeta,
        PYGAME_WINDOW_HEIGHT=config.Config.SCREEN_HEIGHT,
        PYGAME_WINDOW_WIDTH=config.Config.SCREEN_WIDTH,
        PGUI_HEIGHT=600,
        PGUI_WIDTH=800,
    )


if __name__ == '__main__':
    pg_thread = threading.Thread(target=pg)
    pgui_thread = threading.Thread(target=pgui)

    pgui_thread.start()
    pg_thread.start()
