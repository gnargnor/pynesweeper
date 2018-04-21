from game import Game, Board

def test_board_exists():
    """Board can be created."""
    g = Game()
    assert isinstance(g.board, Board)