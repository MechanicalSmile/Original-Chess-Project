from pieces import *
from .rook import Rook

class King(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.icon = "[Kg]"
        self.type = "King"
        self.has_moved = False


    def move_piece(self, color, start_square_info, end_square_info):
        start_square_info.piece = None
        end_square_info.piece = King(color)


    def valid_move(self, start_square_info, end_square_info, squares, has_been_check):
        start_row = start_square_info.row
        start_column = start_square_info.column
        end_row = end_square_info.row
        end_column = end_square_info.column

        row_difference = abs(end_row - start_row)
        column_difference = abs(end_column - start_column)

        # Check if the move is diagonal
        if row_difference == column_difference and row_difference == 1:
            if end_square_info.piece is None or end_square_info.piece.color != start_square_info.piece.color:
                return True

        # Check if the move is horizontal or vertical
        if start_row == end_row or start_column == end_column:
            # Horizontal or vertical move, check for pieces in the path
            if (start_row == end_row and column_difference == 1) or (start_column == end_column and row_difference == 1):
                if end_square_info.piece is None or end_square_info.piece.color != start_square_info.piece.color:
                    return True
            elif has_been_check is False and self.has_moved is False and column_difference == 2:
                if start_square_info.piece.color == "White":
                    if start_square_info.algebraic_notation == "e1" and end_square_info.algebraic_notation == "g1":
                        if squares[7][5].piece == None and squares[7][6].piece == None and squares[7][7].piece.has_moved == False:
                            return True
                    if start_square_info.algebraic_notation == "e1" and end_square_info.algebraic_notation == "c1":
                        if squares[7][1].piece == None and squares[7][2].piece == None and squares[7][3].piece == None and squares[7][0].piece.has_moved == False:
                            return True
                elif start_square_info.piece.color == "Black":
                    if start_square_info.algebraic_notation == "e8" and end_square_info.algebraic_notation == "g8":
                        if squares[0][5].piece == None and squares[0][6].piece == None and squares[0][7].piece.has_moved == False:
                            return True
                    if start_square_info.algebraic_notation == "e8" and end_square_info.algebraic_notation == "c8":
                        if squares[0][1].piece == None and squares[0][2].piece == None and squares[0][3].piece == None and squares[0][0].piece.has_moved == False:
                            return True
                print(f"You may not castle because the rook that will be used to castle has been moved.")
            elif has_been_check is True or self.has_moved is True:
                print(f"You may not castle because either your king has been in check or it has been moved.")
                
        return False  # Invalid move (not horizontal, vertical, or diagonal)
    
    def castle_move(self, color, start_square_info, end_square_info, squares):
        if start_square_info.piece.color == "White":
            if start_square_info.algebraic_notation == "e1" and end_square_info.algebraic_notation == "g1":
                squares[7][7].piece.has_moved == True
                squares[7][5].piece = squares[7][7].piece
                squares[7][7].piece = None
            if start_square_info.algebraic_notation == "e1" and end_square_info.algebraic_notation == "c1":
                squares[7][0].piece.has_moved == True
                squares[7][3].piece = squares[7][0].piece
                squares[7][0].piece = None
        elif start_square_info.piece.color == "Black":
            if start_square_info.algebraic_notation == "e8" and end_square_info.algebraic_notation == "g8":
                squares[0][7].piece.has_moved == True
                squares[0][5].piece = squares[0][7].piece
                squares[0][7].piece = None
            if start_square_info.algebraic_notation == "e8" and end_square_info.algebraic_notation == "c8":
                squares[0][0].piece.has_moved == True
                squares[0][3].piece = squares[0][0].piece
                squares[0][0].piece = None
        end_square_info.piece = start_square_info.piece
        start_square_info.piece = None
        print(f"{color} has Castled")


    def __str__(self):
        return f"King({self.color})"