from battleship.core.ship import Ship


class Board:
    def __init__(self, size: int):
        self.size = size
        self.ship_locations = {}

    def place_ship(self, ship: Ship):
        for cell in ship.get_extent():
            self.ship_locations[cell] = ship
