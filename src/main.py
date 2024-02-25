import threading

import dearpywindow
import pygame_view
from epicycle import State
from settings import epicycle_settings


def main():
    state = State(fps=epicycle_settings.fps)
    pygame_window = pygame_view.create_window(
        state=state,
        width=epicycle_settings.width,
        height=epicycle_settings.height,
    )
    pg_thread = threading.Thread(target=pygame_window.main_loop)
    pgui_thread = threading.Thread(
        target=lambda: dearpywindow.start(
            state=state,
            pygame_window=pygame_window,
            pygame_window_height=epicycle_settings.height,
            pygame_window_width=epicycle_settings.width,
        ),
    )

    pgui_thread.start()
    pg_thread.start()


if __name__ == "__main__":
    main()
