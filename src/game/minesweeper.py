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
    def change_settings(self, option = 'beginner'):
        self.game_over = False
        self.settings = Settings(option)
        self.board = Board(self.settings)
        


class Board:
    """Board class."""

    def __init__(self, settings):

        self.board_exists = True
        layout = list(range(settings.rows * settings.columns))
        self._layout = list(map(self._set_square, layout))
        self._mine_positions =  [randint(0, (settings.rows * settings.columns) - 1) 
                                for mine in range(settings.mines)]
        map(lambda m: self._layout[m]._set_mine(), self._mine_positions)

    # def _set_mine(self, m):
    #         self._layout[m].set_mine()

    def _set_square(self, s):
            s = Square()
            return s
    
    


    # def _set_mines(self, mine_positions, layout):
    #     [layout[pos].set_mine() for pos in mine_positions]



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
 




        
        