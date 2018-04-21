from game import heartbeat, Game

def test_heartbeat():
    h = heartbeat()
    expected = {
        'name': 'Minesweeper'
    }
    assert h == expected
    
def test_game_exists():
    g = Game()
    expected = True
    assert g.game_exists == expected

