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
        self.state = GameState.Setup

    @property
    def instruction(self) -> str:
        match self.state:
            case GameState.Setup:
                instruction = self.board.place_instruction()

            case GameState.Play:
                instruction = "Select a cell to fire upon!"

            case GameState.Done:
                instruction = "Fleet has been sunk!"

        return instruction

    def is_setting_up(self):
        return self.state == GameState.Setup

    def is_playing(self):
        return self.state == GameState.Play

    def is_done(self):
        return self.state == GameState.Done

    def handle_input(self, location: Shot | Placement):
        if self.state == GameState.Setup and isinstance(location, Placement):
            self.board.place_ship(location)
        elif self.state == GameState.Play and isinstance(location, Shot):
            self.board.fire_at(location)

        self.update()

    def update(self):
        self.update_state()

    def update_state(self):
        if self.state == GameState.Setup and self.board.ready:
            self.state = GameState.Play
        elif self.state == GameState.Play and self.board.defeated:
            self.state = GameState.Done
