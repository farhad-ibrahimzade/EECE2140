from view.game_view import GameView
from view.console_board_view import ConsoleBoardView
from model.board import Board
from view.player_symbol import symbols

class ConsoleGameView(GameView):
    def __init__(self, board: Board) -> None:
        board_view = ConsoleBoardView(board)
        super().__init__(board_view)

    def next_player(self, player):
        print(f"Player {symbols[player]}: It's your turn.")

    def next_move(self):
        move = input("Enter your move (row, col): ")
        parts = move.split(",")
        row = int(parts[0])
        col = int(parts[1])
        return row, col
    
    def display_winner(self, winner, is_draw: bool):
        if is_draw:
            print("Draw!")

        else:
            print(f"Player {symbols[winner]} has won the game!")