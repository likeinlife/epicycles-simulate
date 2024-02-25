import threading

import dearpywindow
import pygame_view
from create_points import create_points
from settings import epicycle_settings


def main():
    state = create_points()
    pygame_window = pygame_view.create_window(
        fps=120,
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
