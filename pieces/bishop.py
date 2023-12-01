from pieces import *

class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.icon = "[Bp]"
        self.type = "Bishop"

    def move_piece(self, color, start_square_info, end_square_info):
        start_square_info.piece = None
        end_square_info.piece = Bishop(color)


    def valid_move(self, start_square_info, end_square_info, squares):
        start_row = start_square_info.row
        start_column = start_square_info.column
        end_row = end_square_info.row
        end_column = end_square_info.column

        row_difference = abs(end_row - start_row)
        column_difference = abs(end_column - start_column)

        # Check if the move is diagonal
        if row_difference == column_difference:
            # Diagonal move, check for pieces in the path
            row_step = 1 if end_row > start_row else -1
            column_step = 1 if end_column > start_column else -1

            row, column = start_row + row_step, start_column + column_step
            while row != end_row and column != end_column:
                if squares[row][column].piece is not None:
                    return False  # There's a piece in the way
                row += row_step
                column += column_step

            if end_square_info.piece is None or end_square_info.piece.color != start_square_info.piece.color:
                return True

        return False  # Invalid move (not diagonal)


    def __str__(self):
        return f"Bishop({self.color})"