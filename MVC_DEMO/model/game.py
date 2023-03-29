from model.board import Board
from model.player import Player
from model.game_result import GameResult

class Game:
    def __init__(self, size: int = 3) -> None:
        self.board = Board(size)
        self.size = size
        self.current_player = Player.X

    def change_player(self):
        self.current_player = 3 - self.current_player
        pass

    def make_move(self, row, col):
        self.board[row,col] = self.current_player

    def check_winner(self):
        winner = self.board.check_winner()
        if winner != Board.EMPTY_CELL:
            return winner
        elif self.board.is_full():
            return GameResult.DRAW
        else:
            return GameResult.NONE
