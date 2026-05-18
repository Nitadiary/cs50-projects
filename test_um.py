from um import count

def test_um():
    assert count("UM") == 1
    assert count("um") == 1
    assert count("Um") == 1
    assert count("um um um") == 3
    assert count("your right, um, Im ok") == 1

def test_um_with_mark():
    assert count("UM!!") == 1
    assert count("um,...I guess,...um") == 2
    assert count("number") == 0

def test_um_invalid():
    assert count("mummy") == 0
    assert count("umpire") == 0

