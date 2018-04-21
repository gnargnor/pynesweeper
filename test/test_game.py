from game import heartbeat, Game, Board

def test_heartbeat():
    h = heartbeat()
    expected = {
        'name': 'Minesweeper'
    }
    assert h == expected
    
def test_game_exists():
    g = Game()
    assert g.game_exists == True

def test_game_instantiates_board():
    g = Game()
    assert isinstance(g.board, Board)

def test_lose_ends_game():
    g = Game()
    g.lose()
    assert g.game_over == True

def test_win_ends_game():
    g = Game()
    g.win()
    assert g.game_over == True
