from pieces import *
from board import *

board = Board()

for row in board.squares:
    for square in row:
        print(f"{square.algebraic_notation} is row: {square.row} and column: {square.column} and piece: {square.piece}")