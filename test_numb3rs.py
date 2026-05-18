from numb3rs import validate

def test_valid():
    assert validate("255.255.255.255") == True
    assert validate("127.0.0.1") == True

def test_invalid_range():
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False

def test_valid_format():
    assert validate("cat.dog.cow.bee") == False
    assert validate("127.0.1") == False
    assert validate("127.0.1.1.1") == False
    assert validate("...") == False
    assert validate("000.001.010.100") == False
