from .board import Board
from .settings import Settings

def heartbeat():
    """Returns an object indicating the package is reachable."""

    return {
        'name': 'Minesweeper',
    }

class Game:
    """Game class."""

    def __init__(self):
        self.game_exists = True
        self.game_over = False
        self.settings = Settings()
        self.board = Board(self.settings)

    def lose(self):
        self.game_over = True

    def win(self):
        self.game_over = True

    # Might need a class that exists outside of game?
    # Interface?
    def change_settings(self, option='beginner'):
        self.game_over = False
        self.settings = Settings(option)
        self.board = Board(self.settings)
