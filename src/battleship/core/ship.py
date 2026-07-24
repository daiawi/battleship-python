from dataclasses import dataclass

from battleship.core.actions import Orientation, Placement, Shot


@dataclass(frozen=True)
class ShipInfo:
    name: str
    length: int

class Ship:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size
        self.hits = set()

    def take_hit(self, shot: Shot):
        self.hits.add(shot.cell)

    def get_extent(self, placement: Placement) -> list[tuple[int, int]]:
        row, col = placement.cell

        # Subtracting one biases even size ships to the left
        half = (self.size - 1) // 2

        covered_cells = []

        for offset in range(self.size):
            if placement.orientation == Orientation.HORIZONTAL:
                position = (row, col - half + offset)
            else: 
                position = (row - half + offset, col)
                
            covered_cells.append(position)

        return covered_cells

    def get_info(self):
        return ShipInfo(name=self.name, length=self.size)