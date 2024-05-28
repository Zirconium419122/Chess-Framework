from utilities import *

class Bitboard:
    def __init__(self):
        self.pawns = [0] * 2    # One for white, one for black
        self.knights = [0] * 2  # One for white, one for black
        self.bishops = [0] * 2  # One for white, one for black
        self.rooks = [0] * 2    # One for white, one for black
        self.queens = [0] * 2   # One for white, one for black
        self.kings = [0] * 2    # One for white, one for black

    def initialize_starting_position(self):
        # Set up the starting position of a chess game

        # White and black pawns
        for i in range(decode_square("a2"), decode_square("h2") + 1):
            self.set_piece(1, 0, i)
            self.set_piece(1, 1, i + 40)

        # White and black knights
        self.set_piece(2, 0, decode_square("b1"))
        self.set_piece(2, 0, decode_square("g1"))
        self.set_piece(2, 1, decode_square("b8"))
        self.set_piece(2, 1, decode_square("g8"))

        # White and black bishops
        self.set_piece(3, 0, decode_square("c1"))
        self.set_piece(3, 0, decode_square("f1"))
        self.set_piece(3, 1, decode_square("c8"))
        self.set_piece(3, 1, decode_square("f8"))

        # White and black rooks
        self.set_piece(4, 0, decode_square("a1"))
        self.set_piece(4, 0, decode_square("h1"))
        self.set_piece(4, 1, decode_square("a8"))
        self.set_piece(4, 1, decode_square("h8"))

        # White and black queens
        self.set_piece(5, 0, decode_square("d1"))
        self.set_piece(5, 1, decode_square("d8"))

        # White and black kings
        self.set_piece(6, 0, decode_square("e1"))
        self.set_piece(6, 1, decode_square("e8"))

    def set_piece(self, piece_type, color, square):
        # Set the bit for the given piece type, color, and square to 1
        if isinstance(square, str):
            square = decode_square(square)

        if piece_type == 1:
            self.pawns[color] |= 1 << square
        elif piece_type == 2:
            self.knights[color] |= 1 << square
        elif piece_type == 3:
            self.bishops[color] |= 1 << square
        elif piece_type == 4:
            self.rooks[color] |= 1 << square
        elif piece_type == 5:
            self.queens[color] |= 1 << square
        elif piece_type == 6:
            self.kings[color] |= 1 << square
    
    def clear_square(self, piece_type, color, square):
        # Clear the bit for the given piece type, color, and square
        if piece_type == 1:
            self.pawns[color] &= ~(1 << square)
        elif piece_type == 2:
            self.knights[color] &= ~(1 << square)
        elif piece_type == 3:
            self.bishops[color] &= ~(1 << square)
        elif piece_type == 4:
            self.rooks[color] &= ~(1 << square)
        elif piece_type == 5:
            self.queens[color] &= ~(1 << square)
        elif piece_type == 6:
            self.kings[color] &= ~(1 << square)

    def get_piece(self, piece_type, color, square):
        # Check if the bit for the given piece type, color, and square is 1
        if isinstance(square, str):
            square = decode_square(square)

        if piece_type == 1:
            return (self.pawns[color] & (1 << square)) != 0
        elif piece_type == 2:
            return (self.knights[color] & (1 << square)) != 0
        elif piece_type == 3:
            return (self.bishops[color] & (1 << square)) != 0
        elif piece_type == 4:
            return (self.rooks[color] & (1 << square)) != 0
        elif piece_type == 5:
            return (self.queens[color] & (1 << square)) != 0
        elif piece_type == 6:
            return (self.kings[color] & (1 << square)) != 0

    def move_piece(self, piece_type, color, from_square, to_square):
        # Move a piece from one square to another
        if isinstance(from_square, str):
            from_square = decode_square(from_square)
        if isinstance(to_square, str):
            to_square = decode_square(to_square)

        # Clear the source square
        self.clear_square(piece_type, color, from_square)

        # Set the destination square
        self.set_piece(piece_type, color, to_square)  
 