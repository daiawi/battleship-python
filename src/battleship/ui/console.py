from battleship.core.board import Board
from battleship.core.game import Game
from battleship.core.ship import Ship
from battleship.ui.cell_input import CellInput


class ConsoleUI:
    def __init__(self, game: Game):
        self.game = game
        self.letters = [chr(x + 65) for x in range(self.game.size)]
        self.numbers = [str(x) for x in range(self.game.size)]
        self.input_handler = CellInput(self.letters, self.numbers)

    def run(self):
        while not self.game.is_done():
            self.display()
            position = self.input_handler.take_input()
            self.game.handle_input(position)
            self.game.update()

    def display(self):
        print(" " * 6 + "Battleship")
        print("=" * 22)

        board = self.game.get_board()
        print(self.board_to_str(board))
        print("=" * 22)

    def board_to_str(self, board: Board) -> str:
        output = []

        for row in range(board.size):
            line = [self.letters[row]]

            for col in range(board.size):
                cell = (row, col)
                ship = board.get_cell(cell)

                if ship:
                    line.append(self.ship_to_str(ship, cell))
                else:
                    line.append("~")

            output.append(" ".join(line))

        col_nums = self.numbers.copy()
        col_nums.insert(0," ")
        output.append(" ".join(col_nums))

        return "\n".join(output)

    def ship_to_str(self, ship: Ship, cell: tuple[int, int]) -> str:
        return "S"
