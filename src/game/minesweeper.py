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
    def change_settings(self, option = 'beginner'):
        self.game_over = False
        self.settings = Settings(option)
        self.board = Board(self.settings)
        

class Board:
    """Board class."""

    def __init__(self, settings):
        self.board_exists = True
        self._mine_positions = sample(
            range(settings.rows * settings.columns), settings.mines
            )
        self._layout = self._layout_board(settings, self._mine_positions)
        self._grid = [list(range(idx * settings.columns,
            (idx * settings.columns) + settings.columns)) 
            for idx, row in enumerate(range(0, settings.rows)
            )]


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


    def _get_north_neighbor(self, coordinates):
        row, column = coordinates
        if row > 0:
            return self._grid[row - 1][column]


    def _get_northeast_neighbor(self, coordinates):
        row, column = coordinates
        if (row > 0 and column < (len(self._grid[0]) - 1)):
            return self._grid[row - 1][column + 1]


    def _get_east_neighbor(self, coordinates):
        row, column = coordinates
        if column < (len(self._grid[0]) - 1):
            return self._grid[row][column + 1]

    
    def _get_southeast_neighbor(self, coordinates):
        row, column = coordinates
        if (column < (len(self._grid[0]) - 1) and row < (len(self._grid) - 1)):
            return self._grid[row + 1][column + 1]


    def _get_south_neighbor(self, coordinates):
        row, column = coordinates
        if row < (len(self._grid) - 1):
            return self._grid[row + 1][column]


    def _get_southwest_neighbor(self, coordinates):
        row, column = coordinates
        if (row < (len(self._grid) - 1) and column > 0):
            return self._grid[row + 1][column - 1]

    
    def _get_west_neighbor(self, coordinates):
        row, column = coordinates
        if column > 0:
            return self._grid[row][column - 1]


    def _get_northwest_neighbor(self, coordinates):
        row, column = coordinates
        if (column > 0 and row > 0):
            return self._grid[row - 1][column - 1]


    def open_square(self, coordinates):
        mines_nearby = len(self.check_neighbors(coordinates))
        return mines_nearby


    def check_neighbors(self, coordinates):
        mines = []
        for candidate in self.get_neighbors(coordinates):
            mine_nearby = self._layout[candidate].check()
            if mine_nearby:
                mines.append(candidate)
        return mines


    def get_neighbors(self, coordinates):
        """Returns a list of a square's neighbors.

        Keyword Arguments:
        coordinates: A tuple containing the square's row and column values.
        """
        neighbor_list = [self._get_northwest_neighbor
            , self._get_north_neighbor
            , self._get_northeast_neighbor
            , self._get_west_neighbor
            , self._get_east_neighbor
            , self._get_southwest_neighbor
            , self._get_south_neighbor
            , self._get_southeast_neighbor
            ]
        valid_neighbors = []
        for possible_neighbor in neighbor_list:
            neighborly_contender_value = possible_neighbor(coordinates)
            if neighborly_contender_value is not None:
                valid_neighbors.append(neighborly_contender_value)
        return valid_neighbors


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

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

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
