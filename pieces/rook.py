from pieces import *

class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.icon = "[Rk]"
        self.type = "Rook"
        self.has_moved = False


    def move_piece(self, color, start_square_info, end_square_info):
        end_square_info.piece = start_square_info.piece
        start_square_info.piece = None
    

    def valid_move(self, start_square_info, end_square_info, squares):
        start_row = start_square_info.row
        start_column = start_square_info.column
        end_row = end_square_info.row
        end_column = end_square_info.column

        # Check if the move is horizontal or vertical
        if start_row == end_row or start_column == end_column:
            # Horizontal or vertical move, check for pieces in the path
            if start_row == end_row:
                # Horizontal move
                step = 1 if end_column > start_column else -1
                column = start_column + step
                while column != end_column:
                    if squares[start_row][column].piece is not None:
                        return False  # There's a piece in the way
                    column += step
            else:
                # Vertical move
                step = 1 if end_row > start_row else -1
                row = start_row + step
                while row != end_row:
                    if squares[row][start_column].piece is not None:
                        return False  # There's a piece in the way
                    row += step
            if end_square_info.piece is None or end_square_info.piece.color != start_square_info.piece.color:
                return True

        return False  # Invalid move (not horizontal or vertical)



    def __str__(self):
        return f"Rook({self.color})"