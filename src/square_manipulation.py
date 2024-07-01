from bitboard import Bitboard

def is_square_empty(bitboard: Bitboard, square: str | int):
        # Check if the square is empty (no pieces present)
        return not any(bitboard.get_piece(piece_type, color, square) for piece_type in range(1, 7) for color in range(2))

def is_square_enemy(bitboard: Bitboard, square: str | int, color: int):
    # Check if the square is occupied by an enemy piece
    return any(bitboard.get_piece(piece_type, 1 - color, square) for piece_type in range(1, 7))

def is_square_ally(bitboard: Bitboard, square: str | int, color: int):
    # Check if the square is occupied by an ally piece
    return any(bitboard.get_piece(piece_type, color, square) for piece_type in range(1, 7))

def get_ally_pieces(bitboard: Bitboard, color: str | int):
    ally_pieces_bitboard = 0

    for piece_type in range(1, 7):
        ally_pieces_bitboard |= get_piece_bitboard(bitboard, piece_type, color)

    return ally_pieces_bitboard

def get_piece_bitboard(bitboard: Bitboard, piece_type: int, color: str | int):
    piece_bitboard = 0

    for square in range(64):
        if bitboard.get_piece(piece_type, color, square):
            piece_bitboard |= 1 << square

    return piece_bitboard
