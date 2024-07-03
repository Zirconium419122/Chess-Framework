from bitboard import Bitboard
from square_manipulation import *
from utilities import *

def generate_pawn_moves(color: int, square: str | int, bitboard: Bitboard) -> list:
    moves = []

    if isinstance(square, str):
        square = decode_square(square)

    # Pawn moves forward one square
    single_move = square + (8 if color == 0 else -8)
    if is_square_empty(bitboard, single_move):
        moves.append(single_move)

        # Pawn double move from the starting position
        starting_rank = 1 if color == 0 else 6
        double_move = square + (16 if color == 0 else -16)
        if square // 8 == starting_rank and is_square_empty(bitboard, double_move):
            moves.append(double_move)

    # Pawn captures
    left_capture = single_move - 1
    right_capture = single_move + 1
    if is_square_enemy(bitboard, left_capture, color):
        moves.append(left_capture)
    if is_square_enemy(bitboard, right_capture, color):
        moves.append(right_capture)

    return moves
    
def generate_knight_moves(chess_bitboard: Bitboard, color: int, square: str | int) -> int:
    moves_bitboard = 0

    if isinstance(square, str):
        square = decode_square(square)

    # Convert the square to a bitboard representation
    bitboard = 1 << square

    # Define masks to avoid wrapping
    notAFile = 0xfefefefefefefefe
    notABFile = 0xfcfcfcfcfcfcfcfc
    notHFile = 0x7f7f7f7f7f7f7f7f
    notGHFile = 0x3f3f3f3f3f3f3f3f
    
    # Generate knight moves using bitwise operations
    noNoEa = (bitboard << 17) & notAFile
    noEaEa = (bitboard << 10) & notABFile
    soEaEa = (bitboard >> 6) & notABFile
    soSoEa = (bitboard >> 15) & notAFile
    noNoWe = (bitboard << 15) & notHFile
    noWeWe = (bitboard << 6) & notGHFile
    soWeWe = (bitboard >> 10) & notGHFile
    soSoWe = (bitboard >> 17) & notHFile

    # Combine all moves into a single bitboard
    moves_bitboard = noNoEa | noEaEa | soEaEa | soSoEa | noNoWe | noWeWe | soWeWe | soSoWe

    moves_bitboard &= ~get_ally_pieces(chess_bitboard, color)

    return moves_bitboard

def generate_bishop_moves(color, square, bitboard: Bitboard) -> list:
    moves = []

    if isinstance(square, str):
        square = decode_square(square)

    # Get the column and row of the current square
    col, row = square % 8, square // 8

    # Define the bishop move directions
    bishop_directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

    for direction in bishop_directions:
        dir_col, dir_row = direction
        target_col, target_row = col + dir_col, row + dir_row

        # Continue moving diagonally until reaching the board edge
        while 0 <= target_col < 8 and 0 <= target_row < 8:
            target_square = 8 * target_row + target_col

            # Check if the target square is empty or occupied by an enemy piece
            if not is_square_ally(bitboard, target_square, color):
                moves.append(target_square)

                # If the target square is occupied by an enemy, stop sliding in that direction
                if not is_square_empty(bitboard, target_square):
                    break

            target_col, target_row = target_col + dir_col, target_row + dir_row

    return moves

def generate_rook_moves(color, square, bitboard: Bitboard) -> list:
    moves = []

    if isinstance(square, str):
        square = decode_square(square)

    # Get the column and row of the current square
    col, row = square % 8, square // 8

    # Define the rook move directions
    rook_directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for direction in rook_directions:
        dir_col, dir_row = direction
        target_col, target_row = col + dir_col, row + dir_row

        # Continue moving horizontally or vertically until reaching the board edge
        while 0 <= target_col < 8 and 0 <= target_row < 8:
            target_square = 8 * target_row + target_col
            
            # Check if the target square is empty or occupied by an enemy piece
            if not is_square_ally(bitboard, target_square, color):
                moves.append(target_square)
                
                # If the target square is occupied by an enemy, stop sliding in that direction
                if not is_square_empty(bitboard, target_square):
                    break

            target_col, target_row = target_col + dir_col, target_row + dir_row
        
    return moves

def generate_queen_moves(color, square, bitboard: Bitboard) -> list: 
    moves = []

    if isinstance(square, str):
        square = decode_square(square)
    
    # Get the column and row of the current square 
    col, row = square % 8, square // 8
    
    # Define the queen move directions 
    queen_directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    
    for direction in queen_directions:
        dir_col, dir_row = direction
        target_col, target_row = col + dir_col, row + dir_row
        
        # Continue moving horizontally, vertically, or diagonally until reaching the board edge
        while 0 <= target_col < 8 and 0 <= target_row < 8:
            target_square = 8 * target_row + target_col
            
            # Check if the target square is empty or occupied by an enemy piece
            if not is_square_ally(bitboard, target_square, color):
                moves.append(target_square)
                
                # If the target square is occupied by an enemy, stop sliding in that direction
                if not is_square_empty(bitboard, target_square):
                    break
            
            target_col, target_row = target_col + dir_col, target_row + dir_row

            if is_square_ally(bitboard, target_square, color):
                break
    
    return moves