import random
import chess.svg
from chessboard import display
from time import sleep


board = chess.Board()
randNum = -1
moves={}
game_board = display.start()
while not (board.is_checkmate() or board.is_stalemate()):
    display.check_for_quit()
    sleep(.5)
    move=random.choice(list(board.legal_moves))
    print(board.push(move))

    display.update(board.fen(), game_board)

print("Holyshit it ended")
sleep(10)
