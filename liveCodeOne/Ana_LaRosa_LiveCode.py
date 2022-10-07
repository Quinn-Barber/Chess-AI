import random
import chess.svg
from chessboard import display
from time import sleep

# display time between moves in seconds
Time = 1

# create board object
board = chess.Board()
valid_fen = board.fen()

# Initialization
game_board = display.start()

while True:
    display.check_for_quit()
    legal_moves = list(board.legal_moves)
    enginesmove = random.choice(legal_moves)
    board.san_and_push(enginemove)
    valid_fen = board.fen()
    display.update(valid_fen, game_board)
    sleep(TIME)
