from battleship.core.game import Game
from battleship.ui.console import ConsoleUI


def main():
    game = Game()
    interface = ConsoleUI(game)
    interface.run()

if __name__ == '__main__':
    main()