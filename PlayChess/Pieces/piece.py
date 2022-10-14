""" piece.py
File containing all the piece classes used in drawing_tools.py
"""

import pygame


class Piece:
    def __init__(self, color):
        self.color = color
        self._is_active = True

    @property
    def get_color(self):
        return self.color

    @property
    def is_active(self):
        return self.is_active

    @is_active.setter
    def is_active(self, value):
        self.is_active = value


class Pawn(Piece):
    def __init__(self, color):
        self.piece_type = "PAWN"
        self._piece_image = None
        super().__init__(color)

    @property
    def piece_type(self):
        return self.piece_type

    @piece_type.setter
    def piece_type(self, value):
        self._piece_type = value

    @property
    def piece_image(self):
        if self.color == "BLACK":
            return pygame.image.load("./images/BP.png").convert_alpha()
        else:
            return pygame.image.load("./images/WP.png").convert_alpha()


class Knight(Piece):
    def __init__(self, color):
        self.piece_type = "KNIGHT"
        self._piece_image = None
        super().__init__(color)

    @property
    def piece_type(self):
        return self.piece_type

    @piece_type.setter
    def piece_type(self, value):
        self._piece_type = value

    @property
    def piece_image(self):
        if self.color == "BLACK":
            return pygame.image.load("./images/BN.png").convert_alpha()
        else:
            return pygame.image.load("./images/WN.png").convert_alpha()


class Bishop(Piece):
    def __init__(self, color):
        self.piece_type = "BISHOP"
        self._piece_image = None
        super().__init__(color)

    @property
    def piece_type(self):
        return self.piece_type

    @piece_type.setter
    def piece_type(self, value):
        self._piece_type = value

    @property
    def piece_image(self):
        if self.color == "BLACK":
            return pygame.image.load("./images/BB.png").convert_alpha()
        else:
            return pygame.image.load("./images/WB.png").convert_alpha()


class Rook(Piece):
    def __init__(self, color):
        self.piece_type = "ROOK"
        self._piece_image = None
        super().__init__(color)

    @property
    def piece_type(self):
        return self.piece_type

    @piece_type.setter
    def piece_type(self, value):
        self._piece_type = value

    @property
    def piece_image(self):
        if self.color == "BLACK":
            return pygame.image.load("./images/BR.png").convert_alpha()
        else:
            return pygame.image.load("./images/WR.png").convert_alpha()


class Queen(Piece):
    def __init__(self, color):
        self.piece_type = "QUEEN"
        self._piece_image = None
        super().__init__(color)

    @property
    def piece_type(self):
        return self.piece_type

    @piece_type.setter
    def piece_type(self, value):
        self._piece_type = value

    @property
    def piece_image(self):
        if self.color == "BLACK":
            return pygame.image.load("./images/BQ.png").convert_alpha()
        else:
            return pygame.image.load("./images/WQ.png").convert_alpha()


class King(Piece):
    def __init__(self, color):
        self.piece_type = "KING"
        self._piece_image = None
        super().__init__(color)

    @property
    def piece_type(self):
        return self.piece_type

    @piece_type.setter
    def piece_type(self, value):
        self._piece_type = value

    @property
    def piece_image(self):
        if self.color == "BLACK":
            return pygame.image.load("./images/BK.png").convert_alpha()
        else:
            return pygame.image.load("./images/WK.png").convert_alpha()