class Ship:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size
        self.hits = set()

    def update_center(self, center: tuple[int, int]):
        self.center = center

    def get_extent(self) -> list[tuple[int, int]]:
        row, col = self.center
        start = col - (self.size // 2)

        covered_cells = []

        for offset in range(self.size):
            position = (row, start + offset)
            covered_cells.append(position)

        return covered_cells