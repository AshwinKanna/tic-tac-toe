# settings.py

def initialize_settings():
    """
    @summary: Initialize Display and Resolution settings
    """
    global message, match_winner, match_drawn, current_player
    global player_start_index, players, ttt_board, centric_point_coords
    global display_width, display_height, box_width, box_height
    global white_color, black_color, blue_color, red_color, text_color
    global outer_line_width, inner_line_width, outer_line_points
    global text_font, help_message, text_size, help_message_size
    global text_coords, help_message_coords, text_outline_box
    global vertical_line_1_points, vertical_line_2_points, horizontal_line_1_points, horizontal_line_2_points


    centric_point_coords = [[()]*3, [()]*3, [()]*3]
    ttt_board = [[None]*3, [None]*3, [None]*3]
    players = ['x', 'o']
    player_start_index = 0
    current_player = player_start_index # start with x
    match_winner = None
    match_drawn = False
    message = ""

    display_width = 500
    display_height = 500
    box_width = display_width
    box_height = 420
    white_color = (255, 255, 255)
    black_color = (10,10,10)
    blue_color = (0, 0, 255)
    red_color = (255, 0, 0)
    outer_line_width = 15
    inner_line_width = 10
    outer_line_points = [(0, 0), (box_width, 0), (box_width, box_height), (0, box_height)]
    vertical_line_1_points = [(int(box_width/3), 0), (int(box_width/3), box_height)]
    vertical_line_2_points = [(int(box_width/3) * 2, 0), (int(box_width/3) * 2, box_height)]
    horizontal_line_1_points = [(0, int(box_height/3)), (box_width, int(box_height/3))]
    horizontal_line_2_points = [(0, int(box_height/3) * 2), (box_width, int(box_height/3) * 2)]
    text_font = "comicsansms"
    help_message = "Reset - CTRL+R || Close - CTRL+C"
    text_size = 30
    help_message_size = 14
    text_color = (0, 255, 0)
    text_coords = (int(display_width/2), 450)
    help_message_coords = (int(display_width/2), 490)
    text_outline_box = (0, 428, display_width, 100)

