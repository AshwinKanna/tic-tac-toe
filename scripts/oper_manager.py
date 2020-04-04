# oper_manager.py

# Local application imports
import settings
import surface
import validation

# Third-party installed imports
import pygame as pg


def configure_coords():
    """
    @summary: Prepare coordinates that would be used to draw symbols
    """
    for row_iter in enumerate(settings.centric_point_coords):
        row_index = row_iter[0]
        col_index = 0
        for _ in row_iter[1]:
            x_coord = int((settings.box_width/3) * col_index) + int(settings.box_width/6)
            y_coord = int((settings.box_height/3) * row_index) + int(settings.box_height/6)
            settings.centric_point_coords[row_index][col_index] = (x_coord, y_coord)
            col_index += 1


def change_current_player():
    """
    @summary: Swap both the player's
    """
    if settings.current_player == 0:
        settings.current_player = 1
    elif settings.current_player == 1:
        settings.current_player = 0
    else:
#         log error
        pass


def draw_symbol(row, col, screen):
    """
    @summary: Draw 'x', 'o' on the surface
    """
    if settings.current_player == 0: # For 'x'
        point_coords = settings.centric_point_coords[row][col]
        x_line_1_coords = [(point_coords[0] - 20, point_coords[1] - 50), (point_coords[0] + 20, point_coords[1] + 50)]
        x_line_2_coords = [(point_coords[0] - 20, point_coords[1] + 50), (point_coords[0] + 20, point_coords[1] - 50)]

        pg.draw.line(screen, settings.blue_color, *x_line_1_coords, 5)
        pg.draw.line(screen, settings.blue_color, *x_line_2_coords, 5)
        settings.ttt_board[row][col] = settings.players[settings.current_player].lower()

    elif settings.current_player == 1:   # For 'o'
        pg.draw.circle(screen, settings.blue_color, settings.centric_point_coords[row][col], 20)
        settings.ttt_board[row][col] = settings.players[settings.current_player].lower()

    pg.display.flip()


def reset_game(screen):
    """
    @summary: Reset the game window
    """
    settings.message = ""
    settings.match_drawn = False
    settings.match_winner = None
    settings.current_player = settings.player_start_index
    settings.ttt_board = [[None]*3, [None]*3, [None]*3]

    surface.create_outer_box(screen)
    surface.create_status_pane(screen)


def handle_user_input(screen):
    """
    @summary: Control user inputs
    """
    row = None
    col = None
    pos_x, pos_y = pg.mouse.get_pos()

    if pos_x < int(settings.box_width/3):
        col = 0
    elif pos_x < (int(settings.box_width/3) * 2):
        col = 1
    elif pos_x < settings.box_width:
        col = 2

    if pos_y < int(settings.box_height/3):
        row = 0
    elif pos_y < (int(settings.box_height/3) * 2):
        row = 1
    elif pos_y < settings.box_height:
        row = 2

    if row is None or col is None:
        return

    if settings.ttt_board[row][col] is None:
        draw_symbol(row, col, screen)
        validation.check_result(row, col, screen)
        change_current_player()
        surface.create_status_pane(screen)

