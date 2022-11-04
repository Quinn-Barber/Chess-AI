import chess


def check_if_quasi_stable(board):
    return


def evaluate_position(board):
    """ Evaluates the position of the board based on material
    :param board: board
    :return: evaluation
    """
    if board.outcome():
        return -1000

    fen = board.fen()
    valuations = {'K': 100, 'Q': 9, 'R': 5, 'N': 3, 'B': 3, 'P': 1,  # White
                  'k': -100, 'q': -9, 'r': -5, 'n': -3, 'b': -3, 'p': -1,  # Black
                  }

    evaluation = 0
    for s in fen:
        # Only look at the characters that are actually in the dictionary
        if s in valuations:
            evaluation += valuations[s]
        # Only look at the part of fen that relates to pieces
        if s == ' ':
            break

    factor = 1 if board.turn else -1
    return evaluation * factor


