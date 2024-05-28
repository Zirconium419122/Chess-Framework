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

def print_board(bitboard):
    for color in range(2):
        print(f"{['White', 'Black'][color]} Pawns:")
        print_bitboard(bitboard.pawns[color])
        print(f"{['White', 'Black'][color]} Knights:")
        print_bitboard(bitboard.knights[color])
        print(f"{['White', 'Black'][color]} Bishops:")
        print_bitboard(bitboard.bishops[color])
        print(f"{['White', 'Black'][color]} Rooks:")
        print_bitboard(bitboard.rooks[color])
        print(f"{['White', 'Black'][color]} Queens:")
        print_bitboard(bitboard.queens[color])
        print(f"{['White', 'Black'][color]} Kings:")
        print_bitboard(bitboard.kings[color])
        print()
    
def print_bitboard(bitboard):
    for rank in range(8):
        row = [(bitboard >> (8 * rank + file)) & 1 for file in range(8)]
        print("".join("X" if square else "." for square in row))
