from bitboard import Bitboard

class Chessboard:
    def __init__(self):
        self.bitboard = Bitboard()
        self.current_move = 0
    
    def initialize_board(self):
        self.bitboard.initialize_starting_position()

    def make_move(self, piece_type: int, color: int, from_square: str | int, to_square: str | int):
        self.bitboard.move_piece(piece_type, color, from_square, to_square)
