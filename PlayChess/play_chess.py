#!/usr/bin/env python
""" 
play_chess.py
    Makes a chessboard for the user to play on against a decision
    based chess engine.

    Currently, it uses engine.py to represent the engine that you play against but this can be changed easily
    by looking at the engine_move variable declaration in the game loop.

How to use:
    To use your own engine with this, replace the 'from engine_declan.py import *' statement with your own engine's
    file location. Then replace the 'engine_move = <function>' statement in the game loop with a function from your
    file that returns a legal engine move.

Authors: Declan Cassidy, Milo Posada
POV: Physics & Math major writes Python

TODO: Check if game state is checkmate or draw, so we can exit instead of program crashing
TODO: Allow the player to play as black
TODO: Come up with a more efficient solution for drawing the board after a move is made
      (currently it just draws over the last board lmao)
TODO: Click drag move is the only type that works right now, include other forms
TODO: Drag piece with mouse as you drag
"""
import random

import chess
from pygame.locals import (
    MOUSEBUTTONDOWN,
    MOUSEBUTTONUP,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

from modules.board_tools import *
from modules.drawing_tools import *
from modules.piece import *
from engine import is_stable
from engine import find_depth_move

# Initializes the pygame library
pygame.init()

# Returns a surface to work on
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Initialize board squares and board
chess_board = make_board_squares(SCREEN_WIDTH, SCREEN_HEIGHT)
board = chess.Board()

# Draws squares, then pieces on top of squares
draw_squares(screen, chess_board)
draw_position_by_fen(screen, chess_board, board.fen())

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        if event.type == MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            square1 = get_square_for_position(chess_board, pos).position
        if event.type == MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            square2 = get_square_for_position(chess_board, pos).position

            # Chess.Move throws an error that crashes the program is the move is the same square twice
            if square1 == square2:
                continue
            move_string = square1.lower() + square2.lower()
            move = chess.Move.from_uci(move_string)  # creates player move
            # move.promotion = 5

            moves = list(board.legal_moves)
            if move in moves:
                board.push(move)
            elif chess.Move.from_uci(move_string + 'q') in moves:
                move = chess.Move.from_uci(move_string + 'q')
                board.push(move)
            else:
                # If this line weren't here the engine would just make a move for white when you make an illegal move
                continue

            # Just draw the board again lmao part 1
            draw_squares(screen, chess_board)
            draw_position_by_fen(screen, chess_board, board.fen())

            if board.is_checkmate():
                print("Good game! You Win!")
            elif board.is_stalemate():
                print("Good game! Draw!")
            else:
                # Calculate engine move and make it if not checkmate
                engine_move = find_depth_move(board, 3)
                board.push(engine_move)

            # Just draw the board again lmao part 2
            draw_squares(screen, chess_board)
            draw_position_by_fen(screen, chess_board, board.fen())

            if board.is_checkmate():
                print("Good game! You Lose!")

        elif event.type == QUIT:
            running = False
