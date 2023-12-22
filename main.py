class Bitboard:
    def __init__(self):
        self.pawns = [0] * 2  # One for white, one for black

    def set_piece(self, piece_type, color, square):
        # Set the bit for the given piece type, color, and square to 1
        self.pawns[color] |= 1 << square

    def get_piece(self, piece_type, color, square):
        # Check if the bit for the given piece type, color, and square is 1
        return (self.pawns[color] & (1 << square)) != 0

    def print_board(self):
        for color, bitboard in enumerate(self.pawns):
            print(f"{['White', 'Black'][color]} Pawns:")
            for rank in range(8):
                row = [(bitboard >> (8 * rank + file)) & 1 for file in range(8)]
                print("".join("X" if square else "." for square in row))
            print()


# Example usage:
board = Bitboard()
for i in range(8, 16):
  board.set_piece(1, 0, i)  # Set a white pawn on square 8 - 16
for i in range(48, 56):
    board.set_piece(1, 1, i)  # Set a black pawn on square 51 (7th rank, 4th file)

board.print_board()