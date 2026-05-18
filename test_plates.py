from plates import is_valid
import pytest

def test_valid_digits():
    assert is_valid("DC1W22") == False
    assert is_valid("SFC073") == False
    assert is_valid("LA638") == True
    assert is_valid("SF908") == True

def test_valid_letters():
    assert is_valid("D3456") == False
    assert is_valid("1NY56") == False
    assert is_valid("12NY89") == False
    assert is_valid("LA456") == True
    assert is_valid("SFU456") == True

def test_valid_numeric():
    assert is_valid("DC21!") == False
    assert is_valid("NY 88") == False
    assert is_valid("LA1996") == True
    assert is_valid("LAX789") == True

def test_valid_length():
    assert is_valid("F") == False
    assert is_valid("NEWYORK") == False
    assert is_valid("TX678") == True
    assert is_valid("TXS987") == True

def test_error():
    with pytest.raises(TypeError):
        is_valid(12345)
    with pytest.raises(TypeError):
        is_valid(28937)




