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
        for i in range(self.decode_square("a2"), self.decode_square("h2") + 1):
            self.set_piece(1, 0, i)
            self.set_piece(1, 1, i + 40)

        # White and black knights
        for i in range(2):
            self.set_piece(2, 0, i if i == 1 else i + 6)
            self.set_piece(2, 1, i + 56 if i == 1 else i + 62)
        
        # White and black bishops
        for i in range(2):
            self.set_piece(3, 0, i + 1 if i == 1 else i + 5)
            self.set_piece(3, 1, i + 57 if i == 1 else i + 61)
        
        # White and black rooks
        for i in range(2):
            self.set_piece(4, 0, i - 1 if i == 1 else i + 7)
            self.set_piece(4, 1, i + 55 if i == 1 else i + 63)
        
        # White and black queens
        self.set_piece(5, 0, 4)
        self.set_piece(5, 1, 60)

        # White and black kings
        self.set_piece(6, 0, 3)
        self.set_piece(6, 1, 59)


    def set_piece(self, piece_type, color, square):
        # Set the bit for the given piece type, color, and square to 1
        if isinstance(square, str):
            square = self.decode_square(square)

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
            square = self.decode_square(square)

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
        
    @staticmethod
    def decode_square(coord):
        if len(coord) != 2:
            raise ValueError("Invalid coordinate length")
        
        file_char, rank_char = coord[0].lower(), coord[1]

        if file_char not in "abcdefgh" or rank_char not in "12345678":
            raise ValueError("Invalid coordinate")

        file_index = ord(file_char) - ord("a")
        rank_index = int(rank_char) - 1

        return 8 * rank_index + file_index

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
    
    def move_piece(self, piece_type, color, from_square, to_square):
        # Move a piece from one square to another
        if isinstance(from_square, str):
            from_square = self.decode_square(from_square)
        if isinstance(to_square, str):
            to_square = self.decode_square(to_square)

        # Clear the source square
        self.clear_square(piece_type, color, from_square)

        # Set the destination square
        self.set_piece(piece_type, color, to_square)
    
    def generate_pawn_moves(self, color, square):
        moves = []

        if isinstance(square, str):
            square = self.decode_square(square)

        # Pawn moves forward one square
        single_move = square + (8 if color == 0 else -8)
        if self.is_square_empty(single_move):
            moves.append(single_move)

            # Pawn double move from the starting position
            starting_rank = 1 if color == 0 else 6
            double_move = square + (16 if color == 0 else -16)
            if square // 8 == starting_rank and self.is_square_empty(double_move):
                moves.append(double_move)

        # Pawn captures
        left_capture = single_move - 1
        right_capture = single_move + 1
        if self.is_square_enemy(left_capture, color):
            moves.append(left_capture)
        if self.is_square_enemy(right_capture, color):
            moves.append(right_capture)

        return moves
    
    def generate_knight_moves(self, color, square):
        moves = []
        
        if isinstance(square, str):
            square = self.decode_square(square)

        row = square // 8
        col = square % 8

        # Define the 8 possible moves of a knight
        knight_moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

        for move in knight_moves:
            new_row = row + move[0]
            new_col = col + move[1]

            # Check if the target square is within the board bounds
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                # Check if the target square is empty or occupied by an enemy piece
                target_square = new_row * 8 + new_col
                if not self.is_square_ally(target_square, color):
                    moves.append(target_square)

        return moves

    def generate_bishop_moves(self, color, square):
        moves = []

        if isinstance(square, str):
            square = self.decode_square(square)

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
                if not self.is_square_ally(target_square, color):
                    moves.append(target_square)

                    # If the target square is occupied by an enemy, stop sliding in that direction
                    if not self.is_square_empty(target_square):
                        break

                target_col, target_row = target_col + dir_col, target_row + dir_row

        return moves


    def is_square_empty(self, square):
        # Check if the square is empty (no pieces present)
        return not any(self.get_piece(piece_type, color, square) for piece_type in range(1, 7) for color in range(2))

    def is_square_enemy(self, square, color):
        # Check if the square is occupied by an enemy piece
        return any(self.get_piece(piece_type, 1 - color, square) for piece_type in range(1, 7))
    
    def is_square_ally(self, square, color):
        # Check if the square is occupied by an ally piece
        return any(self.get_piece(piece_type, color, square) for piece_type in range(1, 7))

# Example usage:
chess_board = Bitboard()
chess_board.initialize_starting_position()

# Find legal moves for a white bishop at c1
chess_board.move_piece(1, 0, "d2", "d4")
bishop_moves = chess_board.generate_bishop_moves(0, "c1")
print("Bishop moves:", bishop_moves)
chess_board.move_piece(3, 0, "c1", 38)
chess_board.print_board()







