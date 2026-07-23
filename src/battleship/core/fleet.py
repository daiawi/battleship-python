from battleship.core.ship import Ship


class Fleet:
    def __init__(self) -> None:
        self.ships = [
            Ship("Carrier", 5),
            Ship("Battleship", 4),
            Ship("Cruiser", 3),
            Ship("Submarine", 3),
            Ship("Destroyer", 2),
        ]
        self.num_ships = len(self.ships)
        self.i = 0

    def get_current_ship(self) -> Ship:
        return self.ships[self.i]

    def next_ship(self) -> None:
        self.i = min(self.i + 1, self.num_ships)

    def is_fully_deployed(self) -> bool:
        return self.i == self.num_ships