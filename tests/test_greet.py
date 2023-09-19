from lib.greet import greet


def test_greet():
    assert greet("ben") == 'Hello ben!'
    assert greet('jim') == 'Hello jim!'