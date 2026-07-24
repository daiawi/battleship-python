from enum import Enum, auto

from battleship.core.actions import Placement, Shot
from battleship.core.board import Board


class GameState(Enum):
    Setup = auto()
    Play = auto()
    Done = auto()


class Game:
    def __init__(self):
        self.size = 10
        self.board = Board(self.size)
        self.instruction = "Place Ships!"
        self.state = GameState.Setup

    def is_setting_up(self):
        return self.state == GameState.Setup

    def is_playing(self):
        return self.state == GameState.Play

    def is_done(self):
        return self.state == GameState.Done

    def get_board(self):
        return self.board

    def handle_input(self, data: Shot | Placement):
        if self.state == GameState.Setup and isinstance(data, Placement):
            self.board.place_ship(data)

    def update(self):
        if self.state == GameState.Setup and self.board.ready:
            self.state = GameState.Play