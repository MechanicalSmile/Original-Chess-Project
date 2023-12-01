from pieces import *

class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.icon = "[Kt]"
        self.type = "Knight"
    

    def move_piece(self, color, start_square_info, end_square_info):
        start_square_info.piece = None
        end_square_info.piece = Knight(color)


    def valid_move(self, start_square_info, end_square_info, squares):
        start_row = start_square_info.row
        start_column = start_square_info.column
        end_row = end_square_info.row
        end_column = end_square_info.column

        row_difference = abs(end_row - start_row)
        column_difference = abs(end_column - start_column)

        if (row_difference == 2 and column_difference == 1) or (row_difference == 1 and column_difference == 2):
        # Check if the end square is empty or has an opponent's piece
            if end_square_info.piece is None or end_square_info.piece.color != start_square_info.piece.color:
                return True
            
        return False  # Invalid move


    def __str__(self):
        return f"Knight({self.color})"