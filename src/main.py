from chessboard import Chessboard
from move_generation import generate_knight_moves
from utilities import *

# Example usage:
chess_board = Chessboard()
chess_board.initialize_board()

print_board(chess_board.bitboard)

# Find legal moves for a white knight at g1
chess_board.bitboard.clear_square(2, 0, decode_square("g1"))
knight_moves = generate_knight_moves(chess_board.bitboard, 0, "f3")
print("Knight moves:")
print_bitboard(knight_moves)







