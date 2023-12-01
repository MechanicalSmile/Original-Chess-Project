class Square:
    def __init__(self):
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        self.knight_moves = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
        self.piece = None
        self.row = None
        self.column = None
        self.algebraic_notation = None

    def set_position(self, row, column, algebraic_notation):
        self.row = row
        self.column = column
        self.algebraic_notation = algebraic_notation

    def set_piece(self, piece):
        self.piece = piece

    def remove_piece(self):
        self.piece = None

    def find_threatening_pieces(self, king_square, squares, king_color):

        row = king_square.row
        column = king_square.column
        threatening_pieces = []
        
        #checks if the end square piece is a king and then iterates through all the self.directions of threat to find enemy pieces.
        if king_square.piece or king_square.piece == None:
            for dr, dc in self.directions:
                r, c = row + dr, column + dc
                found_threatening_piece = False
    
                while 0 <= r < 8 and 0 <= c < 8:
                    square = squares[r][c]
                    #If it finds a piece that is not of the kings color it checks the piece type to determine if it has the ability to threaten the king.
                    if square.piece is not None:
                        if square.piece.color != king_color:
                            if (square.piece.type == "Queen" or (square.piece.type == "Rook" and (dr, dc) in [(0, 1), (0, -1), (1, 0), (-1, 0)]) or 
                            (square.piece.type == "Bishop" and (dr, dc) in [(1, 1), (-1, -1), (1, -1), (-1, 1)]) or 
                            (square.piece.type == "Pawn" and abs(r - row) == 1 and abs(c - column) == 1)):
                                #add the threatening piece to the threatening_pieces list with row and column
                                threatening_pieces.append((square.piece, r, c))
                                found_threatening_piece = True
                        break  # Stop in this direction as a piece was found
                    
                    r += dr
                    c += dc
    
                if found_threatening_piece:
                    continue  # Continue checking other self.directions
        
        threatening_knights = self.find_threatening_knights(row, column, king_color, squares)
        threatening_pieces.extend(threatening_knights)

        return threatening_pieces
        


        
    def find_blocking_pieces(self, end_square, squares, king_color):

        row = end_square.row
        column = end_square.column
        blocking_pieces = []

        if end_square.piece == None:
            for dr, dc in self.directions:
                r, c = row + dr, column + dc
                found_blocking_piece = False

                while 0 <= r < 8 and 0 <= c < 8:
                    square = squares[r][c]

                    if square.piece is not None:
                        if square.piece.color == king_color:
                            if (square.piece.type == "Queen" or (square.piece.type == "Rook" and (dr, dc) in [(0, 1), (0, -1), (1, 0), (-1, 0)]) or 
                            (square.piece.type == "Bishop" and (dr, dc) in [(1, 1), (-1, -1), (1, -1), (-1, 1)]) or 
                            (square.piece.type == "Pawn" and ((square.piece.color == "White" and r - row == 1 and column == square.column) or (square.piece.color == "Black" and r - row == -1 and column == square.column)) or 
                            (square.piece.type == "Pawn" and ((square.row == 6 and square.piece.color == "White" and r - row == 2 and column == square.column) or (square.row == 1 and square.piece.color == "Black" and r - row == -2 and column == square.column))))):
                                blocking_pieces.append((square.piece.type, square.algebraic_notation))
                                found_blocking_piece = True
                                
                        break  # Stop in this direction as a piece was found
                    
                    r += dr
                    c += dc
    
                if found_blocking_piece:
                    continue  # Continue checking other self.directions
        
        
        #this code block is for determining whether a piece of the kings color can take the piece that is threatening the king.
        if end_square.piece != None and end_square.piece.color != king_color:
            for dr, dc in self.directions:
                r, c = row + dr, column + dc
                found_blocking_piece = False
    
                while 0 <= r < 8 and 0 <= c < 8:
                    square = squares[r][c]
    
                    if square.piece is not None:
                        if square.piece.color == king_color:
                            if (
                                square.piece.type == "King" and abs(r - row) <= 1 and abs(c - column) <= 1
                            ) or (
                                square.piece.type == "Queen"
                            ) or (
                                square.piece.type == "Rook" and (dr, dc) in [(0, 1), (0, -1), (1, 0), (-1, 0)]
                            ) or (
                                square.piece.type == "Bishop" and (dr, dc) in [(1, 1), (-1, -1), (1, -1), (-1, 1)]
                            ) or (
                                square.piece.type == "Pawn" and abs(r - row) == 1 and abs(c - column) == 1
                            ):
                                blocking_pieces.append((square.piece.type, square.algebraic_notation))
                                found_blocking_piece = True
                        break  # Stop in this direction as a piece was found
                    
                    r += dr
                    c += dc
    
                if found_blocking_piece:
                    continue  # Continue checking other self.directions

        blocking_knights = self.find_blocking_knights(row, column, king_color, squares)
        blocking_pieces.extend(blocking_knights)
        return end_square.algebraic_notation, blocking_pieces



    def find_threatening_knights(self, row, column, king_color, squares):
        """
        Find knight pieces that threaten the square.

        Args:
            row: The row of the square.
            column: The column of the square.
            king_color: The color of the king being threatened.

        Returns:
            A list of threatening knight pieces.
        """
        threatening_knights = []
        
        for dr, dc in self.knight_moves:
            r, c = row + dr, column + dc
            if 0 <= r < 8 and 0 <= c < 8:
                square = squares[r][c]
                if square.piece is not None and square.piece.color != king_color and square.piece.type == "Knight":
                    threatening_knights.append((square.piece, r, c))
        
        return threatening_knights

    def find_blocking_knights(self, row, column, king_color, squares):
        """
        Find knight pieces that can capture the threatening piece.

        Args:
            row: The row of the square.
            column: The column of the square.
            king_color: The color of the king being threatened.

        Returns:
            A list of blocking knight pieces.
        """
        blocking_knights = []
        
        for dr, dc in self.knight_moves:
            r, c = row + dr, column + dc
            if 0 <= r < 8 and 0 <= c < 8:
                square = squares[r][c]
                if square.piece is not None and square.piece.color == king_color and square.piece.type == "Knight":
                    blocking_knights.append((square.piece.type, square.algebraic_notation))
        
        return blocking_knights
