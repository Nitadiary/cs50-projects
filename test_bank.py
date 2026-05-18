import bank
from bank import value
def test_hello():
    assert value("hello") == 0
    assert value("hello, how are you") == 0

def test_h_not_hello():
        assert value("hi") == 20
        assert value("hey there") == 20

def test_others():
        assert value("whats up") == 100
        assert value("good day") == 100

def test_strip_case():
        assert value("  Hello  ") == 0
        assert value("  HI  ") == 20
        assert value("  good day  ") == 100
