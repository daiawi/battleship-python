from enum import Enum, auto

from battleship.core.board import Board


class GameState(Enum):
    Setup = auto()
    Play = auto()


class Game:
    def __init__(self):
        self.size = 10
        self.board = Board(self.size)
        self.instruction = "Place Ships!"
        self.state = GameState.Setup

    def is_over(self):
        return False

    def get_board(self):
        return self.board

    def handle_input(self, position):
        if self.state == GameState.Setup:
            self.board.place_ship(position)