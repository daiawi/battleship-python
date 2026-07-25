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
            if self.game.current_player.is_human:
                self.display()

                valid_input = False
                while not valid_input:
                    
                    if self.game.is_setting_up():
                        action = self.input_handler.take_placement()
                    else:
                        action = self.input_handler.take_shot()

                    valid_input = self.game.handle_input(action)

            self.game.update()

        self.display()

    def display(self):
        print("\n")
        print(" " * 6 + self.game.current_player.name)
        if self.game.is_setting_up():
            self.print_current_player_board()
        else:
            self.print_current_player_board()
            input("Press Enter to continue...")
            self.print_opponent_board()

        print(self.game.instruction)

    def print_current_player_board(self):
        print("=" * 22)
        print(self.board_to_str(self.game.current_player.board, show_ships=True))
        print("=" * 22)

    def print_opponent_board(self):
        print("=" * 22)
        print(self.board_to_str(self.game.opponent.board, show_ships=False))
        print("=" * 22)

    def board_to_str(self, board: Board, show_ships: bool = True) -> str:
        output = []

        for row in range(board.size):
            line = [self.letters[row]]

            for col in range(board.size):
                cell = (row, col)
                ship = board.get_cell(cell)

                if ship:
                    line.append(self.ship_to_str(ship, cell, show_ships))
                elif cell in board.misses:
                    line.append("*")
                else:
                    line.append("~")

            output.append(" ".join(line))

        col_nums = self.numbers.copy()
        col_nums.insert(0," ")
        output.append(" ".join(col_nums))

        return "\n".join(output)

    def ship_to_str(self, ship: Ship, cell: tuple[int, int], show_ship: bool = True) -> str:
        if cell in ship.hits:
            return "X"
        elif show_ship:
            return "S"
        else:
            return "~"
