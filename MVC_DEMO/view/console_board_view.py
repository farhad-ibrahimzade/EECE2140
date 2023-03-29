from view.board_view import BoardView
from model.board import Board
from model.player import Player
from view.player_symbol import symbols

class ConsoleBoardView(BoardView):

    def __init__(self, board: Board) -> None:
        super().__init__(board)

    def display(self):
        header = "-" * (4 * self.board.size + 1)
        print(header)
        for i in range(self.board.size):
            for j in range(self.board.size):
                symbol = symbols[self.board[i,j]]
                print(f"| {symbol} ", end="")

            print("|")

        print(header)
