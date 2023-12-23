class Bitboard:
    def __init__(self):
        self.pawns = [0] * 2    # One for white, one for black
        self.knights = [0] * 2  # One for white, one for black
        self.bishops = [0] * 2  # One for white, one for black
        self.rooks = [0] * 2    # One for white, one for black
        self.queens = [0] * 2   # One for white, one for black
        self.kings = [0] * 2    # One for white, one for black

    def set_piece(self, piece_type, color, square):
        # Set the bit for the given piece type, color, and square to 1
        if piece_type == 1:
            self.pawns[color] |= 1 << square
        elif piece_type == 2:
            self.knights[color] |= 1 << square
        elif piece_type == 3:
            self.knights[color] |= 1 << square
        elif piece_type == 4:
            self.rooks[color] |= 1 << square
        elif piece_type == 5:
            self.queens[color] |= 1 << square
        elif piece_type == 6:
            self.kings[color] |= 1 << square


    def get_piece(self, piece_type, color, square):
        # Check if the bit for the given piece type, color, and square is 1
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

    def print_board(self):
        for color in range(2):
            print(f"{['White', 'Black'][color]} Pawns:")
            self.print_bitboard(self.pawns[color])
            print(f"{['White', 'Black'][color]} Knights:")
            self.print_bitboard(self.knights[color])
            print(f"{['White', 'Black'][color]} Bishops:")
            self.print_bitboard(self.bishops[color])
            print(f"{['White', 'Black'][color]} Rooks:")
            self.print_bitboard(self.rooks[color])
            print(f"{['White', 'Black'][color]} Queens:")
            self.print_bitboard(self.queens[color])
            print(f"{['White', 'Black'][color]} Kings:")
            self.print_bitboard(self.kings[color])
            print()
    
    @staticmethod
    def print_bitboard(bitboard):
        for rank in range(8):
            row = [(bitboard >> (8 * rank + file)) & 1 for file in range(8)]
            print("".join("X" if square else "." for square in row))


# Example usage:
board = Bitboard()
for i in range(8, 16):
    board.set_piece(1, 0, i)  # Set a white pawn on square 8 - 16
for i in range(48, 56):
    board.set_piece(1, 1, i)  # Set a black pawn on square 51 (7th rank, 4th file)

board.set_piece(5, 0, 5)

board.print_board()