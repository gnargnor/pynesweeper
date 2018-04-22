"""Game functionality."""

from collections import namedtuple

def heartbeat():
    """Returns an object indicating the package is reachable."""

    return {
        'name': 'Minesweeper',
    }

class Game:
    """Game class."""

    game_over = False
    default_settings = {}

    def __init__(self, settings = default_settings):
        self.game_exists = True
        self.settings = Settings()
        self.board = Board(settings)

    def lose(self):
        self.game_over = True

    def win(self):
        self.game_over = True

    # Might need a class that exists outside of game?
    def change_settings(self, option = 'beginner'):
        self.settings = Settings(option)


class Board:
    """Board class."""

    layout = []

    def __init__(self, settings):
        self.board_exists = True

class Settings:
    """Game settings."""

    _Settings = namedtuple('Settings', ['mines', 'rows', 'columns'])
    _Settings.__new__.__defaults__ = (10, 10, 10)

    _difficulty = {
        'beginner': _Settings(10, 10, 10),
        'intermediate': _Settings(40, 16, 16),
        'expert': _Settings(99, 16, 30)
    }

    def __init__(self, option = 'beginner'):
        d = self._difficulty[option]
        self.mines = d.mines
        self.rows = d.rows
        self.columns = d.columns
 




        
        