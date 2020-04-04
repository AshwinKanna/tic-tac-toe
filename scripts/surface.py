# surface.py

# Local application imports
import settings

# Third-party installed imports
import pygame as pg


def set_window(screen):
    """
    @summary: Set window properties
    """
    background_color = settings.white_color
    screen.fill(background_color)
    pg.display.set_caption("Tic Tac Toe")
    pg.display.flip()


def create_outer_box(screen):
    """
    @summary: Draw box to enclose all the squares
    """
    screen.fill(settings.white_color)

    # Draw outer line
    pg.draw.lines(screen, settings.black_color, True, settings.outer_line_points, settings.outer_line_width)

    # Draw inner vertical lines
    pg.draw.line(screen, settings.black_color, *settings.vertical_line_1_points, settings.inner_line_width)
    pg.draw.line(screen, settings.black_color, *settings.vertical_line_2_points, settings.inner_line_width)
    # Draw inner horizontal lines
    pg.draw.line(screen, settings.black_color, *settings.horizontal_line_1_points, settings.inner_line_width)
    pg.draw.line(screen, settings.black_color, *settings.horizontal_line_2_points, settings.inner_line_width)

    pg.display.flip()


def create_status_pane(screen):
    """
    @summary: Create status pane on the bottom of the display
    """
    if settings.match_winner != None:
        settings.message = "%s has won!" % (settings.players[settings.match_winner].upper())
#         settings.message = f"{settings.players[settings.match_winner].upper()} has won!"
    else:
        settings.message = "%s's turn" % (settings.players[settings.current_player].upper())
#         settings.message = f"{settings.players[settings.current_player].upper()}'s turn"

    if settings.match_drawn:
        settings.message = 'Match drawn!'

    font_obj = pg.font.SysFont(settings.text_font, settings.text_size)
    text_surface = font_obj.render(settings.message, True, settings.text_color)
    screen.fill(settings.black_color, settings.text_outline_box)
    text_rect = text_surface.get_rect(center=settings.text_coords)
    screen.blit(text_surface, text_rect)

    help_message_font_obj = pg.font.SysFont(settings.text_font, settings.help_message_size)
    help_message_surface = help_message_font_obj.render(settings.help_message, True, settings.white_color)
    help_message_rects = help_message_surface.get_rect(center=settings.help_message_coords)
    screen.blit(help_message_surface, help_message_rects)
    pg.display.flip()

