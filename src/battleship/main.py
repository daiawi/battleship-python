from battleship.core.game import Game
from battleship.core.player import Player
from battleship.ui.console import ConsoleUI


def main():
    size = 7
    game = Game(Player("p1", size), Player("p2", size))
    interface = ConsoleUI(game)
    interface.run()

if __name__ == '__main__':
    main()