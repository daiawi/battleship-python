from battleship.core.board import Board


class Game:
    def __init__(self):
        self.size = 10
        self.board = Board(self.size)
        self.instruction = "Place Ships!"

    def is_over(self):
        return False

    def get_board(self):
        return self.board