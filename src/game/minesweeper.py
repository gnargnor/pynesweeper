"""Game functionality."""

from collections import namedtuple
from random import sample

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
        self._mine_positions =  sample(range(settings.rows * settings.columns), settings.mines)
        self._layout = self._layout_board(settings, self._mine_positions)


    def _layout_board(self, settings, mine_positions):
        mines = sorted(mine_positions, reverse = True)
        print(mine_positions)
        _layout = []
        for idx, s in enumerate(range(settings.rows * settings.columns)):
            s = Square(idx)
            if ((len(mines) > 0) and idx == mines[-1]):
                s.set_mine()
                mines.pop()
            _layout.append(s)
        return _layout


class Square:
    """Square class."""

    _id = None
    _open = False
    _has_mine = False
    _has_flag = False
    _value = None

    def __init__(self, position):
        self._id = position
    
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
