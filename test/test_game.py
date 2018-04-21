from game import heartbeat

def test_heartbeat():
    h = heartbeat()
    expected = {
        'name': 'Minesweeper'
    }
    assert h == expected
    

