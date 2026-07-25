from battleship.core.board import Board


class Player:
    def __init__(self, name: str, board_size: int):
        self.name =  name
        self.board = Board(board_size)

    @property
    def is_human(self):
        return True

    @property
    def ready(self):
        return self.board.is_fleet_deployed()

    @property
    def defeated(self):
        return self.board.is_fleet_sunk()

    