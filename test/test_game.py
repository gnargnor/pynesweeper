"""Minesweeper package unit tests."""

from game import heartbeat, Game, Board, Square, Settings

def test_heartbeat():
    """Package is reachable."""

    h = heartbeat()
    expected = {
        'name': 'Minesweeper'
    }
    assert h == expected


def test_game_exists():
    """Game is instantiatable."""

    g = Game()
    assert isinstance(g, Game)


def test_game_instantiates_board():
    """Board created with Game instantiation."""

    g = Game()
    assert isinstance(g.board, Board)


def test_lose_ends_game():
    """Losing sets game_over to True."""

    g = Game()
    g.lose()
    assert g.game_over == True


def test_win_ends_game():
    """Winning sets game_over to True."""

    g = Game()
    g.win()
    assert g.game_over == True


def test_default_settings():
    """Default game set at beginner."""

    s = Settings()
    assert s.mines == 10
    assert s.columns == 10
    assert s.rows == 10


def test_setting_options():
    """Tests the Settings class instantiation."""

    s = Settings('beginner')
    assert s.mines == 10
    assert s.rows == 10
    assert s.columns == 10
    s = Settings('intermediate')
    assert s.mines == 40
    assert s.rows == 16
    assert s.columns == 16
    s = Settings('expert')
    assert s.mines == 99
    assert s.rows == 16
    assert s.columns == 30


def test_change_settings():
    """Tests game settings changes."""

    g = Game()
    g.lose()
    assert g.game_over == True
    g.change_settings('beginner')
    assert g.settings.mines == 10
    assert g.settings.rows == 10
    assert g.settings.columns == 10
    assert g.game_over == False
    g.lose()
    g.change_settings('intermediate')
    assert g.settings.mines == 40
    assert g.settings.rows == 16
    assert g.settings.columns == 16
    assert g.game_over == False
    g.lose()
    assert g.game_over == True
    g.change_settings('expert')
    assert g.settings.mines == 99
    assert g.settings.rows == 16
    assert g.settings.columns == 30
    assert g.game_over == False


def test_build_board():
    """Board length matches settings."""

    g = Game()
    assert len(g.board._layout) == 100
    g.change_settings('intermediate')
    assert len(g.board._layout) == 256
    g.change_settings('expert')
    assert len(g.board._layout) == 480


def test_mine_count():
    """Tests settings for mine count upon change."""

    g = Game()
    assert len(g.board._mine_positions) == 10
    g.change_settings('intermediate')
    assert len(g.board._mine_positions) == 40
    g.change_settings('expert')
    assert len(g.board._mine_positions) == 99
    g.change_settings('beginner')
    assert len(g.board._mine_positions) == 10

def test_mines_in_board_range():
    """Mine positions don't exceed board length."""

    def assert_position(g):
        """Each mine position within range of appropriate board."""

        for mine in g.board._mine_positions:
            assert mine < len(g.board._layout)
    
    g = Game()
    assert_position(g)
    g.change_settings('intermediate')
    assert_position(g)
    g.change_settings('expert')
    assert_position(g)


def test_open_square_no_mine():
    s = Square()
    s.open()
    assert s._open == True
    assert s._has_mine == False
    
def test_open_square_has_mine():
    s = Square()
    s.set_mine()
    s.open()
    assert s._open == True
    assert s._has_mine == True


def test_layout_all_squares():

    g = Game()
    square_count = 0
    for s in g.board._layout:
        assert isinstance(s, Square)
        square_count = square_count + 1
    assert square_count == 100



