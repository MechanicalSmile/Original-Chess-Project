from pieces import *

class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.icon = "[Pn]"
        self.type = "Pawn"
        self.starting_rows = [6, 1]

    def move_piece(self, color, start_square_info, end_square_info):
        if end_square_info.row == 0 or end_square_info.row == 7:
            promotion = input("Which piece would you like to promote your pawn to? (Queen/Rook/Knight/Bishop)").lower()
            if promotion == "queen":
                start_square_info.piece = None
                end_square_info.piece = Queen(color)
            if promotion == "knight":
                start_square_info.piece = None
                end_square_info.piece = Knight(color)
            if promotion == "rook":
                start_square_info.piece = None
                end_square_info.piece = Rook(color)
            if promotion == "bishop":
                start_square_info.piece = None
                end_square_info.piece = Bishop(color)
        else:
            start_square_info.piece = None
            end_square_info.piece = Pawn(color)
    
    def valid_move(self, start_square_info, end_square_info, squares):
        start_row = start_square_info.row
        start_column = start_square_info.column
        end_row = end_square_info.row
        end_column = end_square_info.column

        if self.color == "White":
            direction = -1
        if self.color == "Black":
            direction = 1

        row_difference = end_row - start_row
        column_difference = abs(end_column - start_column)

        if column_difference == 0:
            if row_difference == direction:
                return True
            elif start_row in self.starting_rows and row_difference == 2 * direction:
                return True
        elif column_difference == 1 and row_difference == direction:
            if end_square_info.piece.color != start_square_info.piece.color:
                return True
            elif end_square_info.piece.color == None:
                return False
            else:
                return False
        else:
            return False
    

    def __str__(self):
        return f"Pawn({self.color})"