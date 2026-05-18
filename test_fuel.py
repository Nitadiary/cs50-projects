from fuel import convert, gauge
import pytest

def test_convert_valid():
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("99/100") == 99
    assert convert("0/2") == 0

def test_convert_invalid():
    with pytest.raises(ValueError):
        convert("2/1")
    with pytest.raises(ValueError):
        convert("-2/4")
    with pytest.raises(ValueError):
        convert("b/g")
    with pytest.raises(ZeroDivisionError):
        convert("2/0")

def test_gauge_e():
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(0) == "E"

def test_gauge_m():
    assert gauge(75) == "75%"
    assert gauge(50) == "50%"

