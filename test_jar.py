from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0
    with pytest.raises(ValueError):
        Jar(-5)
    with pytest.raises(ValueError):
        Jar("two")

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar(9)
    jar.deposit(5)
    assert jar.size == 5
    assert str(jar) == "🍪🍪🍪🍪🍪"
    with pytest.raises(ValueError):
        jar.deposit(6)


def test_withdraw():
    jar = Jar(7)
    jar.deposit(6)
    jar.withdraw(3)
    assert jar.size == 3
    assert str(jar) == "🍪🍪🍪"
    with pytest.raises(ValueError):
        jar.withdraw(7)

