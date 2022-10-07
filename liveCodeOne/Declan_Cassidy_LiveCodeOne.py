import chess.svg
from chessboard import display
import random
from time import sleep

# Intervals between moves
move_interval = 0.1

# Create board and initial visualization
board = chess.Board()
valid_fen = board.fen()
game_board = display.start(valid_fen)

while not display.check_for_quit():
    # Generate engine move
    legal_moves = list(board.legal_moves)
    engine_move = random.choice(legal_moves)
    board.san_and_push(engine_move)

    # Update display of board and wait
    valid_fen = board.fen()
    display.update(valid_fen, game_board)
    sleep(move_interval)

display.terminate()