from battleship.core.board import Board
from battleship.core.game import Game
from battleship.core.ship import Ship


class ConsoleUI:
    def __init__(self, game: Game):
        self.game = game

    def run(self):
        while not self.game.is_over():
            self.display()
            break

    def display(self):
        print(" " * 6 + "Battleship")
        print("=" * 22)

        board = self.game.get_board()
        print(self.board_to_str(board))
        print("=" * 22)
        
    def board_to_str(self, board: Board) -> str:
        output = []
        letters = [chr(x + 65) for x in range(board.size)]

        for row in range(board.size):
            line = [letters[row]]

            for col in range(board.size):
                cell = (row, col)
                if cell in board.ship_locations:
                    ship: Ship = board.ship_locations[cell]
                    line.append(self.ship_to_str(ship, cell))
                else:
                    line.append("~")

            output.append(" ".join(line))

        col_nums = [str(x) for x in range(board.size)]
        col_nums.insert(0," ")
        output.append(" ".join(col_nums))

        return "\n".join(output)

    def ship_to_str(self, ship: Ship, cell: tuple[int, int]) -> str:
        return "S"
