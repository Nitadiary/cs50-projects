import pytest
from working import convert

def test_H():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("8 PM to 8 AM") == "20:00 to 08:00"

def test_H_M():
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("6:30 AM to 7:50 PM") == "06:30 to 19:50"
    assert convert("10:59 AM to 2:10 PM") == "10:59 to 14:10"
    assert convert("12:40 AM to 12:10 PM") == "00:40 to 12:10"
    assert convert("12:40 PM to 12:10 AM") == "12:40 to 00:10"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"

def test_invalid():
    with pytest.raises(ValueError):
        convert("2:60 AM to 8:00 PM")
    with pytest.raises(ValueError):
        convert("0:60 AM to 8:00 PM")
    with pytest.raises(ValueError):
        convert("13:60 AM to 8:00 PM")
    with pytest.raises(ValueError):
        convert("9AM to 5PM")

def test_invalid_f():
    with pytest.raises(ValueError):
        convert("AM 2 to PM 8")
    with pytest.raises(ValueError):
        convert("AM 14:00 to PM 8:60")
    with pytest.raises(ValueError):
        convert("0:60 AM to 8:00 PM")
    with pytest.raises(ValueError):
        convert("13:60 to ")
    with pytest.raises(ValueError):
        convert("10:7 AM - 5:1 PM")
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("09 AM to 5:001 PM")
