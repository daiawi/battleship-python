from enum import Enum, auto

from battleship.core.board import Board
from battleship.core.ship import Ship


class GameState(Enum):
    Setup = auto()
    Play = auto()


class Game:
    def __init__(self):
        self.size = 10
        self.board = Board(self.size)
        self.instruction = "Place Ships!"
        self.state = GameState.Setup
        self.fleet = [
            Ship("Carrier", 5),
            Ship("Battleship", 4),
            Ship("Cruiser", 3),
            Ship("Submarine", 3),
            Ship("Destroyer", 2),
        ]
        self.i = 0

    def is_over(self):
        return False

    def get_board(self):
        return self.board

    def handle_input(self, position):
        if self.state == GameState.Setup:
            ship = self.fleet[0]
            self.board.place_ship(ship, position)