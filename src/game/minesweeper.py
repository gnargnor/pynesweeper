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
        self.board = Board(settings)

    def lose(self):
        self.game_over = True

    def win(self):
        self.game_over = True


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
    }

    def __init__(self, option = 'beginner'):
        d = self._difficulty[option]
        self.mines = d.mines
        self.rows = d.rows
        self.columns = d.columns
 




        
        