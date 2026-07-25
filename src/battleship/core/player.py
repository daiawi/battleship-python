from random import choice, randrange, shuffle

from battleship.core.actions import Orientation, Placement, Shot
from battleship.core.board import Board


class Player:
    def __init__(self, name: str, board_size: int):
        self.name =  name
        self.board = Board(board_size)

    @property
    def is_human(self) -> bool:
        return True

    @property
    def ready(self):
        return self.board.is_fleet_deployed()

    @property
    def defeated(self):
        return self.board.is_fleet_sunk()

    def take_shot(self) -> Shot:
        raise NotImplementedError


class SimpleOpponent(Player):
    def __init__(self, name: str, board_size: int):
        super().__init__(name, board_size)
        self.populate_board()

        self.available_shots = [
            (r, c)
            for r in range(board_size)
            for c in range(board_size)
        ]
        shuffle(self.available_shots)

    @property
    def is_human(self):
        return False

    def populate_board(self):
        while not self.board.is_fleet_deployed():
            location = self.pick_random_cell()
            direction = choice(list(Orientation))

            placement = Placement(cell=location, orientation=direction)

            self.board.place_ship(placement)

    def take_shot(self) -> Shot:
        location = self.available_shots.pop()
        return Shot(cell=location) 

    def pick_random_cell(self) -> tuple[int, int]:
        row = randrange(self.board.size)
        col = randrange(self.board.size)
        return (row, col)