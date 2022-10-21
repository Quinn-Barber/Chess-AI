import random


def evaluate_position(board, fen):
    """ Evaluates the position of the board based on material
    :param fen:
    :return: evaluation
    """
    if(board.is_checkmate()):
        if(board.outcome().winner):
            return 49
        else:
            return -49

    if(board.is_stalemate()):
        return 0

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

    return evaluation

def find_depth_move(board, depth):
    return find_depth_move_recursion(board, depth, depth)

def find_depth_move_recursion(board, depth, returnDepth):
    """ Checks position evaluation out of all possibilities depth moves forward and chooses best move
    :param b:
    :return move:
    """
    if(depth == 0):
        return evaluate_position(board, board.fen())

    moves = list(board.legal_moves)
    vs = {}
    [vs.setdefault(i, []) for i in range(-50, 50, 1)]

    for i, move in zip(range(len(moves)), moves):
        board.push(move)
        v = find_depth_move_recursion(board, depth-1, returnDepth)
        vs[v].append(move)
        board.pop()

    for i in range(-50, 50, 1):
        if not vs[i]: vs.pop(i)

    if(depth == returnDepth):
        if(board.turn):
            return random.choice(vs[max(vs)])
        else:
            return random.choice(vs[min(vs)])
    else:
        if(board.turn):
            return max(vs)
        else:
            return min(vs)