from battleship.core.game import Game
from battleship.core.board import Board
from battleship.core.ship import Ship

class ConsoleUI:
    def __init__(self, game: Game):
        self.game = game

    def run(self):
        while not self.game.is_over():
            self.display()
            break

    def display(self):
        print("Battleship")

        board = self.game.get_board()
        print(self.board_to_str(board))
        
    def board_to_str(self, board: Board) -> str:
        output = []

        for row in range(board.size):
            line = []

            for col in range(board.size):
                cell = (row, col)
                if cell in board.ship_locations:
                    line.append("S")
                else:
                    line.append("~")

            output.append(" ".join(line))

        return "\n".join(output)