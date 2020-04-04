# validation.py

# Local application imports
import settings

# Third-party installed imports
import pygame as pg


def check_horizontal_result(row, screen):
    """
    @summary: Check all squares to the horizontal side of impacted square
    """
    match_won = False

    for col_iter in range(0,3):
        if settings.ttt_board[row][col_iter] and settings.ttt_board[row][col_iter] == settings.players[settings.current_player].lower():
            match_won = True
        else:
            match_won = False
            return False
        
    if match_won:
        start_coord = settings.centric_point_coords[row][0]
        start_coord = (start_coord[0] - 20, start_coord[1])
        end_coord = settings.centric_point_coords[row][2]
        end_coord = (end_coord[0] + 20, end_coord[1])
        pg.draw.line(screen, settings.black_color, start_coord, end_coord, 3)

    return match_won


def check_vertical_result(col, screen):
    """
    @summary: Check all squares to the vertical side of impacted square
    """
    match_won = False

    for row_iter in range(0,3):
        if settings.ttt_board[row_iter][col] and settings.ttt_board[row_iter][col] == settings.players[settings.current_player].lower():
            match_won = True
        else:
            match_won = False
            return False

    if match_won:
        start_coord = settings.centric_point_coords[0][col]
        start_coord = (start_coord[0], start_coord[1] - 20)
        end_coord = settings.centric_point_coords[2][col]
        end_coord = (end_coord[0], end_coord[1] + 20)
        pg.draw.line(screen, settings.black_color, start_coord, end_coord, 3)

    return match_won


def check_diagonal_result(row, col, screen):
    """
    @summary: Check all squares to the diagonal side of impacted square
    """
    # Diagonal check is not needed for other squares
    if abs(row-col) == 1:
        return False

    match_won = False

    def check_first_diagonal():
        nonlocal match_won, screen
        for row_iter, col_iter in zip(range(0,3), range(0,3)):
            if settings.ttt_board[row_iter][col_iter] and settings.ttt_board[row_iter][col_iter] == settings.players[settings.current_player].lower():
                match_won = True
            else:
                match_won = False
                return

        if match_won:
            start_coord = settings.centric_point_coords[0][0]
            end_coord = settings.centric_point_coords[2][2]
            pg.draw.line(screen, settings.black_color, start_coord, end_coord, 3)

    def check_second_diagonal():
        nonlocal match_won, screen
        for row_iter, col_iter in zip(range(0,3), range(2,-1,-1)):
            if settings.ttt_board[row_iter][col_iter] and settings.ttt_board[row_iter][col_iter] == settings.players[settings.current_player].lower():
                match_won = True
            else:
                match_won = False
                return

        if match_won:
            start_coord = settings.centric_point_coords[0][2]
            end_coord = settings.centric_point_coords[2][0]
            pg.draw.line(screen, settings.black_color, start_coord, end_coord, 3)

    if row == 1 and col == 1:
        if not check_first_diagonal():
            check_second_diagonal()
    elif row - col == 0:
        check_first_diagonal()
    elif abs(row - col) == 2:
        check_second_diagonal()
    else:
        # Log
        pass

    return match_won


def check_result(row, col, screen):     
    """
    @summary: Check squares on horizontal, vertical & diagonal sides of impacted square
    """
    if check_horizontal_result(row, screen):
        settings.match_winner = settings.current_player
        return

    if check_vertical_result(col, screen):
        settings.match_winner = settings.current_player
        return

    if check_diagonal_result(row, col, screen):
        settings.match_winner = settings.current_player
        return

    if(all([all(row_iter) for row_iter in settings.ttt_board]) and settings.match_winner is None ):
        settings.match_drawn = True

