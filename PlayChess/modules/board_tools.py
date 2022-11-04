class BoardSquare:
    def __init__(self, x_start, y_start, width_height, color, position):
        """ Initializes a square on a chess board
        :param x_start: top left x coord of square
        :param y_start: top left y coord of square
        :param width_height: side length of square
        :param color: black or white square
        :param position: A1-H8 square notation for making moves
        """
        self.x_start = x_start
        self.y_start = y_start
        self.width_height = width_height
        self.color = color
        self.position = position
        self.piece = None


def create_board_square(screen_width, screen_height, x_array, y_array, color, position):
    """ Makes a board square object
    :param screen_width: side length of each square
    :param screen_height: height of display window
    :param x_array: x
    :param y_array: y
    :param color: color of square
    :param position: A1-H8 board notation
    :return: BoardSquare object
    """
    if screen_width < screen_height or screen_width == screen_height:
        width_height = screen_width / 8
    else:
        width_height = screen_height / 8

    x_coordinate = x_array * width_height
    y_coordinate = y_array * width_height

    return BoardSquare(x_coordinate, y_coordinate, width_height, color, position)


def get_square_for_position(chess_board, pos):
    """ Gets the square at the mouse's position
    :param chess_board: 2D list of BoardSquare objects
    :param pos: mouse position (x, y)
    :return: BoardSquare object at mouse position
    """
    for row in chess_board:
        if row[0].y_start < pos[1] < row[0].y_start + row[0].width_height:
            for square in row:
                if square.x_start < pos[0] < square.x_start + square.width_height:
                    return square


def alternate_color(color):
    """ Changes color between WHITE and BLACK
    :param color: WHITE or BLACK
    :return: opposite of input
    """
    if color == "BLACK":
        return "WHITE"
    else:
        return "BLACK"


def make_board_squares(screen_width, screen_height):
    """ Creates list of BoardSquare objects to represent the chess board
    :param screen_width:
    :param screen_height:
    :return: 2D list of BoardSquare objects 8x8
    """
    chess_board = []
    square_color = "BLACK"
    for y in range(8):
        chess_row = []
        square_color = alternate_color(square_color)
        for x in range(8):
            position = chr(x + 65) + str(8 - y)
            chess_row.append(create_board_square(screen_width, screen_height, x, y, square_color, position))
            square_color = alternate_color(square_color)
        chess_board.append(chess_row)
    return chess_board