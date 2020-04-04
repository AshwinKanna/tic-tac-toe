# init_app.py

# Standard libary imports
import time

# Local application imports
import settings
import surface
import oper_manager


# Third-party installed imports
import pygame as pg
from pygame.locals import (
    K_ESCAPE,
    KMOD_CTRL,
    KEYDOWN,
    QUIT,
    MOUSEBUTTONDOWN,
    K_c,
    K_r,
)


def initialize_display():
    """
    @summary: 
    """
    pg.init()
    pg.display.init()
    screen = pg.display.set_mode((settings.display_width, settings.display_height))
    return screen


def manage_execution(screen):
    """
    @summary: Main controller method
    """
    running = True
    while running:
        for event in pg.event.get():

            if event.type == KEYDOWN:
                # CTRL + C to close
                if event.key == K_c and (pg.key.get_mods() & KMOD_CTRL):
                    running = False
                # CTRL + R to reset
                elif event.key == K_r and (pg.key.get_mods() & KMOD_CTRL):
                    oper_manager.reset_game(screen)

            elif event.type == MOUSEBUTTONDOWN:
                oper_manager.handle_user_input(screen)
                if settings.match_winner != None or settings.match_drawn:
                    time.sleep(2)
                    oper_manager.reset_game(screen)

            elif event.type == QUIT:
                running = False

        pg.display.flip()

    pg.quit()
    return


if __name__ == '__main__':
    settings.initialize_settings()
    screen = initialize_display()
    surface.set_window(screen)
    surface.create_outer_box(screen)
    surface.create_status_pane(screen)

    oper_manager.configure_coords()
    manage_execution(screen)

    print("Completed execution")