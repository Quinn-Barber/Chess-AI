import chess
from modules.engine_tools import evaluate_position
from modules.engine_tools import check_if_quasi_stable


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