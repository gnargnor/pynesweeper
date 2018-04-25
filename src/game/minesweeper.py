"""Game functionality."""

from collections import namedtuple
from random import randint

def heartbeat():
    """Returns an object indicating the package is reachable."""

    return {
        'name': 'Minesweeper',
    }

class Game:
    """Game class."""

    game_over = False

    def __init__(self):
        self.game_exists = True
        self.settings = Settings()
        self.board = Board(self.settings)

    def lose(self):
        self.game_over = True

    def win(self):
        self.game_over = True

    # Might need a class that exists outside of game?
    # Interface?
    def change_settings(self, option = 'beginner'):
        self.game_over = False
        self.settings = Settings(option)
        self.board = Board(self.settings)
        

class Board:
    """Board class."""

    def __init__(self, settings):

        self.board_exists = True
        self._layout = list(map(self._set_square, ([None] * (settings.rows * settings.columns))))
        self._mine_positions =  [randint(0, len(self._layout) - 1) 
                                for mine in ([None] * settings.mines)]
        for mp in self._mine_positions:
            self._layout[mp].set_mine()

    def _set_square(self, s):
            s = Square()
            return s


class Square:
    """Square class."""

    _open = False
    _has_mine = False
    _has_flag = False
    _value = None

    def __init__(self):
        pass
    
    def set_mine(self):
        self._has_mine = True

    def open(self):
        if (self._has_flag or self._open):
            return
        self._open = True
        return self._has_mine

    def check(self):
        return self._has_mine


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
        