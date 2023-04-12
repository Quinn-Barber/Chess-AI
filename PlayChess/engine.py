import random

import chess

# Milo is trash
# Quinn best chess player of all time

global abPruning
global positionsChecked
global positionsPruned
def evaluate_position(board, fen):
    """ Evaluates the position of the board based on material
    :param fen:
    :return: evaluation
    """
    if board.is_checkmate():
        if board.outcome().winner:
            return 49
        else:
            return -49

    if board.is_stalemate():
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
    global abPruning
    global positionsChecked
    global positionsPruned
    abPruning = {}
    [abPruning.setdefault(i+1, []) for i in range(depth)]
    positionsChecked = 0
    positionsPruned = 0
    ans = find_depth_move_recursion(board, 0, depth)
    print(positionsChecked, " checked positions | ", positionsPruned, " pruned positions")
    if ans is []:
        return list(board.legal_moves)[0]
    return ans

def find_depth_move_recursion(board, depth, returnDepth):
    """ Checks position evaluation out of all possibilities depth moves forward and chooses best move
    :param b:
    :return move:
    """
    # We want to set the pruning number, the given depth can have a max
    # or min value associated with it depending on whose turn it is,
    # in which we can prune (not search) any branches if they are lower than
    # the max or higher than the min number.
    # Special cases arise based on quasi-stability of the board;
    # for now, we will ignore this.
    global abPruning
    global positionsChecked
    global positionsPruned
    if depth % 2 == 1:
        # Black just moved, favor negative values
        if not abPruning[depth]:
            abPruning[depth] = evaluate_position(board, board.fen())
        else:
            abPruning[depth] = min(abPruning[depth], evaluate_position(board, board.fen()))
    else:
        if depth != 0:
            # White just moved, favor positive values
            if not abPruning[depth]:
                abPruning[depth] = evaluate_position(board, board.fen())
            else:
                abPruning[depth] = max(abPruning[depth], evaluate_position(board, board.fen()))

    searchTree = True
    if depth != 0 and is_stable(board):
        if abPruning[depth] != evaluate_position(board, board.fen()):
            searchTree = False # If you want to test without alpha-beta pruning, set this to True!

    positionsChecked += 1
    if not searchTree:
        positionsPruned += 1

    if depth == returnDepth or not searchTree or len(list(board.legal_moves)) == 0:
        return evaluate_position(board, board.fen())

    moves = list(board.legal_moves)
    vs = {}
    [vs.setdefault(i, []) for i in range(-50, 50, 1)]

    for i, move in zip(range(len(moves)), moves):
        board.push(move)
        v = find_depth_move_recursion(board, depth+1, returnDepth)
        if v != -1000:
            vs[v].append(move)
        board.pop()

    for i in range(-50, 50, 1):
        if not vs[i]: vs.pop(i)

    if depth == 0:
        if board.turn:
            return random.choice(vs[max(vs)])
        else:
            return random.choice(vs[min(vs)])
    else:
        if len(vs) == 0:
            return -1000
        if board.turn:
            return max(vs)
        else:
            return min(vs)

# Determines Stability
# New engine must always evaluate at least two moves ahead
# New engine must always evaluate positions where this function returns 1 (UNLESS PAST 10 DEPTH)
# Overall depth will vary from 2-10 but be much quicker to calculate
def is_stable(board):
    """
    Returns 0 if not quasi stable
        - If any piece is attacked by another of lower value
        - If any piece has more attackers than defenders
        - If any check exists from opponent
    Returns 1 if quasi stable
        - None of the above
    :param board:
    :return: 1 | 0
    """
    # Edge cases (need to be dealt with externally i.e: display game result and such)
    if board.is_check() or board.is_checkmate() or board.is_stalemate():
        return 0
    for piece in board.piece_map():
        if board.piece_at(piece).color == chess.WHITE:
            attackerTurn = chess.BLACK
            defenderTurn = chess.WHITE
        else:
            attackerTurn = chess.WHITE
            defenderTurn = chess.BLACK
        attackers = []
        for attacker in board.attackers(attackerTurn, piece):
            if board.piece_at(attacker).piece_type == 1:
                attackers.append(1)
            elif board.piece_at(attacker).piece_type == 2:
                attackers.append(3)
            elif board.piece_at(attacker).piece_type == 3:
                attackers.append(3)
            elif board.piece_at(attacker).piece_type == 4:
                attackers.append(5)
            elif board.piece_at(attacker).piece_type == 5:
                attackers.append(9)
            elif board.piece_at(attacker).piece_type == 6:
                attackers.append(49)
        attackers.sort()
        defenders = []
        for defender in board.attackers(defenderTurn, piece):
            if board.piece_at(defender).piece_type == 1:
                defenders.append(1)
            elif board.piece_at(defender).piece_type == 2:
                defenders.append(3)
            elif board.piece_at(defender).piece_type == 3:
                defenders.append(3)
            elif board.piece_at(defender).piece_type == 4:
                defenders.append(5)
            elif board.piece_at(defender).piece_type == 5:
                defenders.append(9)
            elif board.piece_at(defender).piece_type == 6:
                defenders.append(49)
        defenders.sort()
        puaValue = 1
        if board.piece_at(piece).piece_type == 2:
            puaValue = 3
        elif board.piece_at(piece).piece_type == 3:
            puaValue = 3
        elif board.piece_at(piece).piece_type == 4:
            puaValue = 5
        elif board.piece_at(piece).piece_type == 5:
            puaValue = 9
        elif board.piece_at(piece).piece_type == 6:
            puaValue = 49
        if len(attackers) == len(defenders) or len(defenders) > len(attackers):
            for i in range(len(attackers)):
                if i == 0:
                    if puaValue > attackers[i]:
                        return 0
                else:
                    if defenders[i-1] > attackers[i]:
                        return 0
        else:
            return 0;
    return 1

