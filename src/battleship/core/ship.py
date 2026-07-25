from battleship.core.actions import Orientation, Placement, Shot


class Ship:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size
        self.hits = set()

    def take_hit(self, shot: Shot):
        is_new = shot.cell not in self.hits
        self.hits.add(shot.cell)
        return is_new

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

    def is_sunk(self):
        return len(self.hits) == self.size