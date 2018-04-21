"""Game functionality"""

def heartbeat():
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
        
        