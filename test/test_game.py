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


# may not need to keep track of mine positions after setup
# depending on how check nearby works
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
    s = Square(position = 0)
    s.open()
    assert s._open == True
    assert s._has_mine == False
    
def test_open_square_has_mine():
    s = Square(position = 0)
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


def test_squares_have_ids():
    g = Game()
    for s in g.board._layout:
        assert isinstance(s._id, int)


def test_count_mines():
    g = Game()
    mine_count = 0
    for s in g.board._layout:
        if (s.check()):
            mine_count += 1
    assert mine_count == 10

    g.change_settings('intermediate')
    mine_count = 0
    for s in g.board._layout:
        if (s.check()):
            mine_count += 1
    assert mine_count == 40

    g.change_settings('expert')
    mine_count = 0
    for s in g.board._layout:
        if (s.check()):
            mine_count += 1
    assert mine_count == 99


def test_grid_layout():
    g = Game()
    assert len(g.board._grid) == 10
    g.change_settings('intermediate')
    assert len(g.board._grid) == 16
    g.change_settings('expert')
    assert len(g.board._grid) == 16


def test_neighbors():
    g = Game()
    # when passed row, column, return the index? Why? who knows.  I'm just pissin in the wind man.
    assert g.board.get_east_neighbor((0, 0)) == 1
    assert g.board.get_east_neighbor((0, 9)) == None

    assert g.board.get_west_neighbor((0, 0)) == None
    assert g.board.get_west_neighbor((0, 9)) == 8

    assert g.board.get_north_neighbor((1, 1)) == 1
    assert g.board.get_north_neighbor((0, 1)) == None

    assert g.board.get_south_neighbor((9, 4)) == None
    assert g.board.get_south_neighbor((3, 3)) == 43

    assert g.board.get_northeast_neighbor((9, 9)) == None
    assert g.board.get_northeast_neighbor((4, 5)) == 36

    assert g.board.get_southeast_neighbor((9, 0)) == None
    assert g.board.get_southeast_neighbor((4, 0)) == 51
    assert g.board.get_southeast_neighbor((3, 9)) == None

    # assert g.board.get_neighbors((0, 0)) == [1, 10, 11]
    # assert g.board.get_neighbors((1, 1)) == [0, 1, 2, 10, 12, 20, 21, 22]
    # assert g.board.get_neighbors((0, 9)) == [8, 18, 19]
