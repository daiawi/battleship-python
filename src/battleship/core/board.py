from battleship.core.ship import Ship


class Board:
    def __init__(self, size: int):
        self.size = size
        self.ship_locations = {}

    def place_ship(self, ship: Ship, position: tuple[int, int]):
        ship.update_center(position)
        for cell in ship.get_extent():
            self.ship_locations[cell] = ship

    def get_cell(self, cell: tuple[int, int]) -> Ship | None:
        return self.ship_locations.get(cell)