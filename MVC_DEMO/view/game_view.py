from abc import ABC, abstractmethod
from view.board_view import BoardView

class GameView(ABC):
    def __init__(self, board_view: BoardView) -> None:
        self.board_view = board_view

    @abstractmethod
    def next_player(self, player):
        pass

    @abstractmethod
    def next_move(self):
        pass

    def display_board(self):
        self.board_view.display()

    @abstractmethod
    def display_winner(self):
        pass