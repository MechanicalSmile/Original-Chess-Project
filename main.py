from board.board import Board
from user.user import User
import random
import time

class __Main__:
    def __init__(self):
        self.player1 = User()
        self.player2 = User()
        self.board = Board()
        self.initialized = False
        self.running = True
        self.turn = 0
        self.players_turn = None

    def set_player_names(self):
        if self.player1.username is None:
            self.player1.username = input("Player one please enter your name: ")
        if self.player2.username is None:
            self.player2.username = input("Player two please enter your name: ")

    def choose_heads_tails(self):
        if self.player1.coinflip_choice is None:
            self.player1.coinflip_choice = input("Player one, choose Heads or Tails? ").strip().lower()
            if self.player1.coinflip_choice in ("heads", "tails"):
                if self.player1.coinflip_choice == "heads":
                    self.player2.coinflip_choice =  "tails"
                elif self.player1.coinflip_choice == "tails":
                    self.player2.coinflip_choice = "heads"
            else:
                self.player1.coinflip_choice = None

    def flip_coin(self):
        if self.player1.coinflip_choice != None:
            if self.player1.chose_first is None and self.player2.chose_first is None:
                flip_result = random.randint(1,2)
                if self.player1.coinflip_choice == "heads" and flip_result == 1 or self.player1.coinflip_choice == "tails" and flip_result == 2:
                    coin_flip_result = True
                else:
                    coin_flip_result = False
                if coin_flip_result == True and self.player1.chose_first == None:
                    self.player1.chose_first = input("Player one, you won the coin flip. Would you like to go first? (Y/N)").strip().lower()
                    if self.player1.chose_first in ("y", "n"):
                        if self.player1.chose_first == "y":
                            self.player1.color = "White"
                            self.player2.color = "Black"
                            self.players_turn = "Player One"
                        else:
                            self.player1.color = "Black"
                            self.player2.color = "White"
                            self.players_turn = "Player Two"
                    else:
                        print("Invalid Choice")
                        self.player1.chose_first = None
                        self.player2.chose_first = None

                elif coin_flip_result == False and self.player2.chose_first == None:
                    self.player2.chose_first = input("Player two, you won the coin flip. Would you like to go first? (Y/N)").strip().lower()
                    if self.player2.chose_first in ("y", "n"):
                        if self.player2.chose_first == "y":
                            self.player2.color = "White"
                            self.player1.color = "Black"
                            self.players_turn = "Player Two"
                        else:
                            self.player2.color = "Black"
                            self.player1.color = "White"
                            self.players_turn = "Player One"
                    else:
                        print("Invalid Choice")
                        self.player1.chose_first = None
                        self.player2.chose_first = None

    def initialize_board(self):
        if self.player1.color != None and self.player2.color != None and self.initialized == False:
            if self.player1.color == "Black":
                print("Player one")
            if self.player2.color == "Black":
                print("Player two")
            self.board.initialize(self.player1.color, self.player2.color)
            if self.player1.color == "White":
                print("Player one")
            if self.player2.color == "White":
                print("Player two")
            self.initialized = True

    def update_board(self):
        self.board.update_board()

    def find_notation(self, data, target_notation):
        for item in data:
            if target_notation in item:
                return True


game = __Main__()


while game.running == True:
    available_moves = []
    game.set_player_names()
    game.choose_heads_tails()
    game.flip_coin()
    game.initialize_board()
    time.sleep(1)
    if game.board.stalemate_turns == 0:
        print("Stalemate!")

    while game.players_turn == "Player One":
        print(f"{game.player1.username}'s turn")
        if game.player1.is_check is True:
            print("You are in check move or protect your king.")
            while True:
                starting_square = input("Which piece would you like to move?:")
                if len(starting_square) == 2 and starting_square[0] in "abcdefgh" and starting_square[1] in "12345678":
                    if king_moves:
                        if starting_square == king_square:
                            break
                    if blocking_pieces:
                        for element in blocking_pieces:
                            location, pieces = element
                            can_piece_block = game.find_notation(pieces, starting_square)
                            if can_piece_block is True:
                                break
                        if can_piece_block is True:
                                break
            while True:
                ending_square = input("Where would you like to move it?: ")
                if len(starting_square) == 2 and starting_square[0] in "abcdefgh" and starting_square[1] in "12345678":
                    if starting_square == king_square:
                        if ending_square in king_moves:
                            break
                        else:
                            print("Invalid Destination")
                    elif ending_square == location:
                        break
            
            move = game.board.move_piece(starting_square, ending_square, game.player1.color, game.player1.has_been_check)
            game.player1.is_check = False
            
            if move == True:
                game.update_board()
                check_list = game.board.is_check(game.player2.color)
                if check_list:
                    check, threatening_pieces, king_square, king_color = check_list
                    if check == True:
                        check_mate = game.board.is_checkmate(king_color, king_square, threatening_pieces)
                        if check_mate is True:
                           print("Player one wins the game!")
                        else:
                            king_square, king_moves, blocking_pieces = check_mate
                            game.player2.is_check = True
                            game.player2.has_been_check = True
                            game.players_turn = "Player Two"
                            continue
                else:
                    game.players_turn = "Player Two"
            else:
                pass

        else:
            game.turn += 1

            while True:
                starting_square = input("Which piece would you like to move?: ")
                if len(starting_square) == 2 and starting_square[0] in "abcdefgh" and starting_square[1] in "12345678":
                    break
                else:
                    print("Invalid input, please use valid algeraic notation")
            while True:
                ending_square = input("Where would you like to move it?: ")
                if len(starting_square) == 2 and starting_square[0] in "abcdefgh" and starting_square[1] in "12345678":
                    break
                else:
                    print("Invalid input, please use valid algeraic notation")

            move = game.board.move_piece(starting_square, ending_square, game.player1.color, game.player1.has_been_check)
            game.player1.is_check = False
            
            if move == True:
                game.update_board()
                check_list = game.board.is_check(game.player2.color)
                if check_list:
                    check, threatening_pieces, king_square, king_color = check_list
                    if check == True:
                        check_mate = game.board.is_checkmate(king_color, king_square, threatening_pieces)
                        if check_mate is True:
                           print("Player one wins the game!")
                        else:
                            king_square, king_moves, blocking_pieces = check_mate
                            game.player2.is_check = True
                            game.players_turn = "Player Two"
                            continue
                else:
                    game.players_turn = "Player Two"
            else:
                pass
        stalemate = game.board.is_stalemate()
        if stalemate is True:
            print("The game has ended in a Stalemate")
            break


    time.sleep(1)
    if game.board.stalemate_turns == 0:
        print("Stalemate!")
    while game.players_turn == "Player Two":
        print(f"{game.player2.username}'s turn")
        if game.player2.is_check is True:
            print("You are in check move or protect your king.")
            while True:
                starting_square = input("Which piece would you like to move?:")
                if len(starting_square) == 2 and starting_square[0] in "abcdefgh" and starting_square[1] in "12345678":
                    if king_moves:
                        if starting_square == king_square:
                            break
                    if blocking_pieces:
                        for element in blocking_pieces:
                            location, pieces = element
                            can_piece_block = game.find_notation(pieces, starting_square)
                            if can_piece_block is True:
                                break
                        if can_piece_block is True:
                                break
            while True:
                ending_square = input("Where would you like to move it?: ")
                if len(starting_square) == 2 and starting_square[0] in "abcdefgh" and starting_square[1] in "12345678":
                    if starting_square == king_square:
                        if ending_square in king_moves:
                            break
                        else:
                            print("Invalid Destination")
                    elif ending_square == location:
                        break
            move = game.board.move_piece(starting_square, ending_square, game.player2.color, game.player2.has_been_check)
            game.player2.is_check = False

            if move == True:
                game.update_board()
                check_list = game.board.is_check(game.player1.color)
                if check_list:
                    check, threatening_pieces, king_square, king_color = check_list
                    if check == True:
                        check_mate = game.board.is_checkmate(king_color, king_square, threatening_pieces)
                        if check_mate == True:
                            print(f"{game.player2.username}wins the game!")
                        else:
                            king_square, king_moves, blocking_pieces = check_mate
                            game.player1.is_check = True
                            game.players_turn = "Player One"
                else:
                    game.players_turn = "Player One"
            else:
                pass

        else:
            game.turn += 1
            while True:
                starting_square = input("Which piece would you like to move?: ")
                if len(starting_square) == 2 and starting_square[0] in "abcdefgh" and starting_square[1] in "12345678":
                    break
                else:
                    print("Invalid input, please use valid algeraic notation")
            while True:
                ending_square = input("Where would you like to move it?: ")
                if len(starting_square) == 2 and starting_square[0] in "abcdefgh" and starting_square[1] in "12345678":
                    break
                else:
                    print("Invalid input, please use valid algeraic notation")

            move = game.board.move_piece(starting_square, ending_square, game.player2.color, game.player2.has_been_check)
            game.player2.is_check = False

            if move == True:
                game.update_board()
                check_list = game.board.is_check(game.player1.color)
                if check_list:
                    check, threatening_pieces, king_square, king_color = check_list
                    if check == True:
                        check_mate = game.board.is_checkmate(king_color, king_square, threatening_pieces)
                        if check_mate == True:
                            print(f"{game.player2.username}wins the game!")
                        else:
                            king_square, king_moves, blocking_pieces = check_mate
                            game.player1.is_check = True
                            game.player1.has_been_check = True
                            game.players_turn = "Player One"
                else:
                    game.players_turn = "Player One"
            else:
                pass
        stalemate = game.board.is_stalemate()
        if stalemate is True:
            print("The game has ended in a Stalemate")
            break
            