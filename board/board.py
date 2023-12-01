from board.square import Square
from pieces import *

class Board:
    def __init__(self):
        self.stalemate_turns = 50
        self.squares = [[Square() for _ in range(8)] for _ in range(8)]
        # Set the position attributes for each Square
        self.set_square_positions()
        # Initialize the starting positions of the pieces
        self.initialize_start_positions()

    def set_square_positions(self):
        for row in range(8):
            for col in range(8):
                algebraic_notation = f"{chr(ord('a') + col)}{8 - row}"
                self.squares[row][col].set_position(row, col, algebraic_notation)

    def initialize_start_positions(self):
        starting_positions = {
            "White": {
                "Pawns": ["A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2"],
                "Rooks": ["A1", "H1"],
                "Knights": ["B1", "G1"],
                "Bishops": ["C1", "F1"],
                "Queens": ["D1"],
                "Kings": ["E1"],
            },
            "Black": {
                "Pawns": ["A7", "B7", "C7", "D7", "E7", "F7", "G7", "H7"],
                "Rooks": ["A8", "H8"],
                "Knights": ["B8", "G8"],
                "Bishops": ["C8", "F8"],
                "Queens": ["D8"],
                "Kings": ["E8"],
            }
        }

        for color, pieces in starting_positions.items():
            for piece_type, positions in pieces.items():
                for position in positions:
                    row = 8 - int(position[1])
                    col = ord(position[0]) - ord('A')
                    piece = self.create_piece(piece_type, color)
                    self.squares[row][col].piece = piece

    def create_piece(self, piece_type, color):
        # Create an instance of the specified piece type and color
        if piece_type == "Pawns":
            return Pawn(color)
        elif piece_type == "Rooks":
            return Rook(color)
        elif piece_type == "Knights":
            return Knight(color)
        elif piece_type == "Bishops":
            return Bishop(color)
        elif piece_type == "Queens":
            return Queen(color)
        elif piece_type == "Kings":
            return King(color)



    def initialize(self, player1, player2):
        column_labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        row_labels = ['8', '7', '6', '5', '4', '3', '2', '1']

        # Print column labels (letters)
        print("    " + "    ".join(column_labels))

        # Create empty squares
        for row_num, row in enumerate(self.squares):
            print(row_labels[row_num], end=' ')
            for square in row:
                if square.piece:
                    print(square.piece.icon, end=' ')
                else:
                    print("[  ]", end=' ')
            print(row_labels[row_num])
        print("    " + "    ".join(column_labels))

    def update_board(self):
        column_labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        row_labels = ['8', '7', '6', '5', '4', '3', '2', '1']

        # Print column labels (letters)
        print("    " + "    ".join(column_labels))

        for row_num, row in enumerate(self.squares):
            print(row_labels[row_num], end=' ')
            for square in row:
                if square.piece:
                    print(square.piece.icon, end=' ')
                else:
                    print("[  ]", end=' ')
            print(row_labels[row_num])

    def move_piece(self, start_pos, end_pos, color, has_been_check):
        # Get the piece on the starting square
        start_square_info = None
        end_square_info = None
        for row in self.squares:
            for square in row:
                if square.algebraic_notation == start_pos:
                    start_square_info = square
                    if square.piece == None or square.piece.color != color:
                        print(f"{square.algebraic_notation} does not contain a piece that you can move.")
                        return
                if square.algebraic_notation == end_pos:
                    end_square_info = square

        piece = start_square_info.piece
        piece_type = start_square_info.piece.type
        if piece_type == "King":
            valid = piece.valid_move(start_square_info, end_square_info, self.squares, has_been_check)
            color = start_square_info.piece.color
            if valid == True:
                if start_square_info.piece.color == "White" and start_square_info.algebraic_notation in ["e1", "e8", "d1", "d8"] and end_square_info.algebraic_notation in ["g1", "g8", "b1", "b8"]:
                    piece.castle_move(color, start_square_info, end_square_info, self.squares)
                else:
                    piece.move_piece(color, start_square_info, end_square_info)
                    piece.has_moved = True
                return True
            if valid == False:
                print("Invalid move, Try again")
                return False
            
        if piece_type == "Queen":
            color = start_square_info.piece.color
            valid = piece.valid_move(start_square_info, end_square_info, self.squares)
            if valid == True:
                piece = start_square_info.piece
                piece.move_piece(color, start_square_info, end_square_info)
                cause_check = self.is_check(color)
                if cause_check is not None and True in cause_check:
                    piece.move_piece(color, end_square_info, start_square_info)
                    print("You cannot move this piece as it would result in your king being in check.")
                    return False
                else:
                    return True
            if valid == False:
                print("Invalid move, Try again")

        if piece_type == "Rook":
            valid = piece.valid_move(start_square_info, end_square_info, self.squares)
            color = start_square_info.piece.color
            if valid == True:
                piece = start_square_info.piece
                piece.move_piece(color, start_square_info, end_square_info)
                cause_check = self.is_check(color)
                if cause_check is not None and True in cause_check:
                    piece.move_piece(color, end_square_info, start_square_info)
                    print("You cannot move this piece as it would result in your king being in check.")
                    return False
                else:
                    piece.has_moved = True
                    return True
            if valid == False:
                print("Invalid move, Try again")

        if piece_type == "Bishop":
            valid = piece.valid_move(start_square_info, end_square_info, self.squares)
            color = start_square_info.piece.color
            if valid == True:
                piece = start_square_info.piece
                piece.move_piece(color, start_square_info, end_square_info)
                cause_check = self.is_check(color)
                if cause_check is not None and True in cause_check:
                    piece.move_piece(color, end_square_info, start_square_info)
                    print("You cannot move this piece as it would result in your king being in check.")
                    return False
                else:
                    return True
            if valid == False:
                print("Invalid move, Try again")

        if piece_type == "Knight":
            valid = piece.valid_move(start_square_info, end_square_info, self.squares)
            color = start_square_info.piece.color
            if valid == True:
                piece = start_square_info.piece
                piece.move_piece(color, start_square_info, end_square_info)
                cause_check = self.is_check(color)
                if cause_check is not None and True in cause_check:
                    piece.move_piece(color, end_square_info, start_square_info)
                    print("You cannot move this piece as it would result in your king being in check.")
                    return False
                else:
                    return True
            if valid == False:
                print("Invalid move, Try again")

        if piece_type == "Pawn":
            valid = piece.valid_move(start_square_info, end_square_info, self.squares)
            if valid == True:
                piece = start_square_info.piece
                piece.move_piece(color, start_square_info, end_square_info)
                cause_check = self.is_check(color)
                if cause_check is not None and True in cause_check:
                    piece.move_piece(color, end_square_info, start_square_info)
                    print("You cannot move this piece as it would result in your king being in check.")
                    return False
                else:
                    return True
            if valid == False:
                print("Invalid move, Try again")

    def is_check(self, king_color):
        # Find the king's position
        king_square = None
        for row, row_squares in enumerate(self.squares):
            for column, square in enumerate(row_squares):
                if square.piece is not None and square.piece.type == "King" and square.piece.color == king_color:
                    king_square = square
                    threatening_pieces = square.find_threatening_pieces(king_square, self.squares, king_color)
                    for piece, piece_row, piece_column in threatening_pieces:
                        print(f"{piece} is threatening the square {self.squares[row][column].algebraic_notation} from {self.squares[piece_row][piece_column].algebraic_notation}")
                    if threatening_pieces:
                        return True, threatening_pieces, king_square, king_color
                if king_square:
                    break
    
    def get_valid_king_moves(self, king_square, king_color):
        valid_moves = []
        for dr, dc in king_square.directions:
            r, c = king_square.row + dr, king_square.column + dc
            if 0 <= r < 8 and 0 <= c < 8:
                simulate_move_square = self.squares[r][c]
                if simulate_move_square.piece is None:
                    not_valid_move = simulate_move_square.find_threatening_pieces(simulate_move_square, self.squares, king_color)
                    if not not_valid_move:
                        valid_moves.append(simulate_move_square.algebraic_notation)
                elif simulate_move_square.piece.color != king_color:
                    not_valid_move = simulate_move_square.find_threatening_pieces(simulate_move_square, self.squares, king_color)
                    if not not_valid_move:
                        valid_moves.append(simulate_move_square.algebraic_notation)
        return valid_moves

    def find_blocking_pieces_between(self, king_square, threatening_pieces, king_color, valid_moves):
        blocking_pieces = []
        for piece, threatening_row, threatening_column in threatening_pieces:
            next_square_row = king_square.row
            next_square_column = king_square.column
            if threatening_row > king_square.row:
                row_step = 1
                if threatening_column > king_square.column:
                    column_step = 1
                elif threatening_column < king_square.column:
                    column_step = -1
                else:
                    column_step = 0
            elif threatening_row < king_square.row:
                row_step = -1
                if threatening_column > king_square.column:
                    column_step = 1
                elif threatening_column < king_square.column:
                    column_step = -1
                else:
                    column_step = 0
            else:
                row_step = 0
                if threatening_column > king_square.column:
                    column_step = 1
                elif threatening_column < king_square.column:
                    column_step = -1
                else:
                    column_step = 0
            while next_square_row != threatening_row or next_square_column != threatening_column:
                next_square_row += row_step
                next_square_column += column_step
                square = self.squares[next_square_row][next_square_column]
                found_blockers = square.find_blocking_pieces(square, self.squares, king_color)
                if not valid_moves:
                    for i, item in enumerate(found_blockers):
                        if len(item) == 2 and any(piece[0] == 'King' for piece in item[1]):
                            found_blockers[i] = (item[0], [(piece_name, piece_position) for piece_name, piece_position in item[1] if piece_name != 'King'])
                blocking_pieces.append(found_blockers)
        return blocking_pieces

    def is_checkmate(self, king_color, king_square, threatening_pieces):
        valid_moves = self.get_valid_king_moves(king_square, king_color)
        blocking_pieces = self.find_blocking_pieces_between(king_square, threatening_pieces, king_color, valid_moves)

        if not valid_moves:
            if not blocking_pieces:
                return True
            else:
                return king_square.algebraic_notation, valid_moves, blocking_pieces
        else:
            return king_square.algebraic_notation, valid_moves, blocking_pieces
   
    def is_stalemate(self):
        white_king_square = None
        white_king_color = None
        black_king_square = None
        black_king_color = None
        white_pieces_left = 0
        black_pieces_left = 0
        for row, row_squares in enumerate(self.squares):
            for column, square in enumerate(row_squares):
                if square.piece is not None and square.piece.type == "King":
                    king_square, king_color = square, square.piece.color
                    if square.piece.color == "White":
                        white_king_square = square
                        white_king_color = square.piece.color
                        white_pieces_left += 1
                    if square.piece.color == "Black":
                        black_king_square = square
                        black_king_color = square.piece.color
                        black_pieces_left += 1
                elif square.piece is not None:
                    if square.piece.color == "White":
                        white_pieces_left += 1
                    if square.piece.color == "Black":
                        black_pieces_left += 1
        if white_pieces_left == 1 and black_pieces_left == 1:
            return True
        if white_pieces_left == 1 or black_pieces_left == 1:
            no_valid_moves_white = self.get_valid_king_moves(white_king_square, white_king_color)
            no_valid_moves_black = self.get_valid_king_moves(black_king_square, black_king_color)
            if not no_valid_moves_white or not no_valid_moves_black:
                return True
            self.stalemate_turns -= 1
            print(f"Turns until Stalemate: {self.stalemate_turns}")