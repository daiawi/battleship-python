from battleship.core.game import Game
from battleship.core.player import Player
from battleship.ui.console import ConsoleUI


def main():
    game = Game(Player("p1",10), Player("p2", 10))
    interface = ConsoleUI(game)
    interface.run()

if __name__ == '__main__':
    main()