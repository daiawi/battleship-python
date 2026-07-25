from battleship.core.actions import Placement, Shot
from battleship.core.fleet import Fleet
from battleship.core.ship import Ship


class Board:
    def __init__(self, size: int):
        self.size = size
        self.fleet = Fleet()
        self.ship_locations = {}
        self.misses = set()

    def is_fleet_deployed(self):
        return self.fleet.is_fully_deployed()

    def is_fleet_sunk(self):
        return self.fleet.is_fully_destroyed()

    def place_instruction(self) -> str:
        ship = self.fleet.get_current_ship()        
        return f"Place your {ship.name} ({ship.size})"

    def place_ship(self, position: Placement) -> bool:
        ship = self.fleet.get_current_ship()

        if not self.valid_placement(ship, position):
            return False

        for cell in ship.get_extent(position):
            self.ship_locations[cell] = ship

        self.fleet.next_ship()
        return True

    def fire_at(self, shot: Shot):
        ship = self.get_cell(shot.cell)

        if not ship:
            self.misses.add(shot.cell)
            return True

        return ship.take_hit(shot)

    def valid_placement(self, ship: Ship, position: Placement) -> bool:
        for cell in ship.get_extent(position):
            # Check if cell is occupied
            if self.get_cell(cell):
                return False

            # Check if cell is on board
            if not self.in_bounds(cell):
                return False
            
        return True

    def in_bounds(self, cell: tuple[int, int]) -> bool:
        row, col = cell
        return 0 <= row < self.size and 0 <= col < self.size

    def get_cell(self, cell: tuple[int, int]) -> Ship | None:
        return self.ship_locations.get(cell)