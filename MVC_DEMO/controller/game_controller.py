from model.game import Game
from view.game_view import GameView
from model.game_result  import GameResult

class GameController:
    def __init__(self, model: Game, view: GameView) -> None:
        self.model = model
        self.view = view

    def run_game(self):
        self.view.display_board()

        game_ended = False
        
        while not game_ended:
            self.view.next_player(self.model.current_player)
            row, col = self.view.next_move()
            self.model.make_move(row, col)
            self.view.display_board()
            result = self.model.check_winner()
            if result != GameResult.NONE:
                self.view.display_winner(self.model.current_player, result == GameResult.DRAW)
                game_ended = True
            else:
                self.model.change_player()

            