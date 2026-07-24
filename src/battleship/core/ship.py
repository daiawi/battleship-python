from battleship.core.actions import Placement


class Ship:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size
        self.hits = set()

    def get_extent(self, center: Placement) -> list[tuple[int, int]]:
        row, col = center.cell
        start = col - (self.size // 2)

        covered_cells = []

        for offset in range(self.size):
            position = (row, start + offset)
            covered_cells.append(position)

        return covered_cells