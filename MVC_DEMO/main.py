from model.game import Game
from view.console_game_view import ConsoleGameView
from controller.game_controller import GameController


model = Game()
view = ConsoleGameView(model.board)
controller = GameController(model, view)

controller.run_game()