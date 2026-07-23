from battleship.core.ship import Ship


class Board:
    def __init__(self, size: int):
        self.size = size
        self.ship_locations = {}

    def place_ship(self, ship: Ship, covered_cells: list[tuple[int, int]]):
        for cell in covered_cells:
            self.ship_locations[cell] = ship
