from battleship.core.board import Board
from battleship.core.game import Game
from battleship.core.ship import Ship


class ConsoleUI:
    def __init__(self, game: Game):
        self.game = game
        self.letters = [chr(x + 65) for x in range(self.game.size)]
        self.numbers = [str(x) for x in range(self.game.size)]

    def run(self):
        while not self.game.is_over():
            self.display()
            self.take_input()
            break

    def display(self):
        print(" " * 6 + "Battleship")
        print("=" * 22)

        board = self.game.get_board()
        print(self.board_to_str(board))
        print("=" * 22)

    def take_input(self):
        print(self.game.instruction)

        while True:
            cell_code = input("Input Cell: ")

            if self.validate_input_cell(cell_code):
                break

            print("Sorry, try again!")

        cell = self.parse_input_cell(cell_code) 
        print(cell)


    def validate_input_cell(self, cell_code: str) -> bool:
        if not cell_code:
            return False

        letter_valid = cell_code[0].upper() in self.letters
        number_valid = cell_code[1:] in self.numbers
        
        return letter_valid and number_valid

    def parse_input_cell(self, cell_code: str) -> tuple[int, int]:
        let_str = cell_code[0].upper()
        num_str = cell_code[1]

        row = self.letters.index(let_str)
        col = self.numbers.index(num_str)

        return (row, col)

    def board_to_str(self, board: Board) -> str:
        output = []

        for row in range(board.size):
            line = [self.letters[row]]

            for col in range(board.size):
                cell = (row, col)
                if cell in board.ship_locations:
                    ship: Ship = board.ship_locations[cell]
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
