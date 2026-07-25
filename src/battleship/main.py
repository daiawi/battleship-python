from battleship.core.game import Game
from battleship.core.player import Player, SimpleOpponent
from battleship.ui.console import ConsoleUI


def main():
    size = 7
    game = Game(Player("p1", size), SimpleOpponent("p2", size))
    interface = ConsoleUI(game)
    interface.run()

if __name__ == '__main__':
    main()