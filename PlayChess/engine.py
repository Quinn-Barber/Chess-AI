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

# Determines Stability
# New engine must always evaluate at least two moves ahead
# New engine must always evaluate positions where this function returns 1 (UNLESS PAST 10 DEPTH)
# Overall depth will vary from 2-10 but be much quicker to calculate
def not_stable(board):
    """
    Returns 1 if not quasi stable
        - If any piece is attacked by another of lower value
        - If any piece has more attackers than defenders
        - If any check exists from opponent
    Returns 0 if quasi stable
        - None of the above
    :param board:
    :return: 1 | 0
    """
    # Edge cases (need to be dealt with externally i.e: display game result and such)
    # if board.is_check() or board.is_stalemate() or board.is_fivefold_repetition() or board.is_seventyfive_moves() or board.is_insufficient_material() or board.is_checkmate()
        # return 1
    # loop through every spot on the board:
        # if it contains a piece:
            # loop through board.attackers(chess.WHITE, square) and board.attackers(chess.BLACK, square) and add them to different saved values
            # if these values are not equal
                # return 1
            # else if these values are not 0
                # if any of the attackers is less valuable than attacked piece
                    # return 1
        # else
            # if there is a check from this square
                # if this square is controlled by an opponent piece
                    # return 1
    # end loop
    # return 0

