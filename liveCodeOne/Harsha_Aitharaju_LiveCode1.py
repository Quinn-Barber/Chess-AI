import chess
import chessboard
from chessboard import display
import random
from time import sleep

print("Hello")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
TIME = 1
board = chess.Board()
valid_fen = board.fen()
game_board = display.start()

while not display.check_for_quit():
    legal_moves = list(board.legal_moves)
    enginemove = random.choice(legal_moves)
    board.san_and_push(enginemove)
    valid_fen = board.fen()
    display.update(valid_fen, game_board)
    sleep(TIME)