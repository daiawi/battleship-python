from battleship.core.board import Board


class Game:
    def __init__(self):
        self.board = Board(10)

    def is_over(self):
        return False

    def get_board(self):
        return self.board