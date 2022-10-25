import chess

def evaluate_position(board):
    """ Evaluates the position of the board based on material
    :param b: board
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


def find_best_move(board, depth):
    # When the depth is at its end, return evaluation + last move
    if depth == 0:
        return {evaluate_position(board): [board.move_stack[-1]]}

    evals = {}
    for move in list(board.legal_moves):
        board.push(move)
        lowest_eval = 0
        if board.is_checkmate():
            lowest_eval = 1000
        else:
            for response in list(board.legal_moves):
                board.push(response)
                eval = list(find_best_move(board, depth - 1).keys())[0]
                board.pop()

                lowest_eval = lowest_eval if lowest_eval < eval else eval

        if lowest_eval not in list(evals.keys()):
            evals[lowest_eval] = []

        evals[lowest_eval].append(move)
        board.pop()

    return {max(evals): evals[max(evals)]}


board = chess.Board("8/8/R5pr/6p1/5pPk/5P1p/5P1K/8 b - - 1 1")
moves = find_best_move(board, 3)
print(moves)
