from PlayChess.Pieces.piece import *


def draw_position_by_fen(screen, chess_board, fen):
    """ Draws pieces on BoardSquare objects using a FEN string
    :param screen: pygame screen object
    :param chess_board: 2D list of BoardSquare objects
    :param fen: FEN stirng
    :return: None
    """
    fen = fen.split()
    fen = fen[0].split('/')
    row, col = 0, 0
    for fen_row in fen:
        for c in fen_row:
            square = chess_board[row][col]
            if c == 'p':
                square.piece = Pawn('BLACK')
                screen.blit(square.piece.piece_image, (square.x_start+10, square.y_start+10))
            elif c == 'n':
                chess_board[row][col].piece = Knight('BLACK')
                screen.blit(square.piece.piece_image, (square.x_start+10, square.y_start+10))
            elif c == 'b':
                chess_board[row][col].piece = Bishop('BLACK')
                screen.blit(square.piece.piece_image, (square.x_start+10, square.y_start+10))
            elif c == 'r':
                chess_board[row][col].piece = Rook('BLACK')
                screen.blit(square.piece.piece_image, (square.x_start+10, square.y_start+10))
            elif c == 'q':
                chess_board[row][col].piece = Queen('BLACK')
                screen.blit(square.piece.piece_image, (square.x_start+10, square.y_start+10))
            elif c == 'k':
                chess_board[row][col].piece = King('BLACK')
                screen.blit(square.piece.piece_image, (square.x_start+10, square.y_start+10))
            elif c == 'P':
                square.piece = Pawn('WHITE')
                screen.blit(square.piece.piece_image, (square.x_start+10, square.y_start+10))
            elif c == 'N':
                chess_board[row][col].piece = Knight('WHITE')
                screen.blit(square.piece.piece_image, (square.x_start+10, square.y_start+10))
            elif c == 'B':
                chess_board[row][col].piece = Bishop('WHITE')
                screen.blit(square.piece.piece_image, (square.x_start+10, square.y_start+10))
            elif c == 'R':
                chess_board[row][col].piece = Rook('WHITE')
                screen.blit(square.piece.piece_image, (square.x_start+10, square.y_start+10))
            elif c == 'Q':
                chess_board[row][col].piece = Queen('WHITE')
                screen.blit(square.piece.piece_image, (square.x_start+10, square.y_start+10))
            elif c == 'K':
                chess_board[row][col].piece = King('WHITE')
                screen.blit(square.piece.piece_image, (square.x_start+10, square.y_start+10))
            else:
                col += int(c) - 1
            col += 1
        row += 1
        col = 0

        pygame.display.flip()


def draw_squares(screen, chess_board):
    """ Draws squares on pygame screen
    :param screen: pygame screen object
    :param chess_board: 2D list of BoardSquare objects
    :return: None
    """
    for row in chess_board:
        for square in row:
            surf = pygame.Surface((square.width_height, square.width_height))

            if square.color == "WHITE":
                surf.fill((238,238,210))
            else:
                surf.fill((118,150,86))

            screen.blit(surf, (square.x_start, square.y_start))

    pygame.display.flip()
