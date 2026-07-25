from enum import Enum, auto

from battleship.core.actions import Placement, Shot
from battleship.core.player import Player


class GameState(Enum):
    Setup = auto()
    Play = auto()
    Done = auto()


class Game:
    def __init__(self, player1: Player, player2: Player):
        self.size = 10
        self.players = (player1, player2)
        self.player_idx = 0
        self.state = GameState.Setup
        self.winner = None

    @property
    def current_player(self):
        return self.players[self.player_idx]

    @property
    def opponent(self):
        return self.players[1 - self.player_idx]

    @property
    def instruction(self) -> str:
        match self.state:
            case GameState.Setup:
                instruction = self.current_player.board.place_instruction()

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

    def next_player(self):
        self.player_idx = 1 - self.player_idx

    def handle_input(self, location: Shot | Placement) -> bool:
        if self.state == GameState.Setup and isinstance(location, Placement):
            return self.current_player.board.place_ship(location)
        elif self.state == GameState.Play and isinstance(location, Shot):
            return self.opponent.board.fire_at(location)
        return False

    def update(self):
        self.update_state()

    def update_state(self):
        if self.state == GameState.Setup and self.current_player.ready:
            self.next_player()
            if all(player.ready for player in self.players):
                self.state = GameState.Play

        elif self.state == GameState.Play:
            if self.opponent.defeated:
                self.winner = self.current_player.name
                self.state = GameState.Done
            self.next_player()

