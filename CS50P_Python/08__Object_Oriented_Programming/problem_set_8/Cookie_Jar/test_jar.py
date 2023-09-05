# pytest CS50P_Python/08__Object_Oriented_Programming/problem_set_8/Cookie_jar/test_jar.py

from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar.size == 0
    assert jar.capacity == 12

    jar_6 = Jar(6)
    assert jar_6.capacity == 6


def test_init_negative(capfd):
    # test for ValueError
    with pytest.raises(ValueError) as e:
        Jar(-2)
    assert str(e.value) == "Capacity cannot be negative"


def test_deposit():
    jar = Jar()
    jar.deposit(4)
    assert jar.size == 4


def test_deposit_negative(capfd):
    # test for ValueError
    with pytest.raises(ValueError) as e:
        jar = Jar()
        jar.deposit(-2)
    assert str(e.value) == "Cannot deposit a negative numer"


def test_deposit_overflow(capfd):
    # test for ValueError
    with pytest.raises(ValueError) as e:
        jar = Jar()
        jar.deposit(22)
    assert str(e.value) == "Cannot deposit more than capacity"


def test_withdraw():
    jar = Jar()
    jar.deposit(4)
    jar.withdraw(2)
    assert jar.size == 2


def test_withdraw_negative(capfd):
    # test for ValueError
    with pytest.raises(ValueError) as e:
        jar = Jar()
        jar.deposit(4)
        jar.withdraw(-2)
    assert str(e.value) == "Cannot withdraw a negative numer"


def test_deposit_underflow(capfd):
    # test for ValueError
    with pytest.raises(ValueError) as e:
        jar = Jar()
        jar.deposit(4)
        jar.withdraw(6)
    assert str(e.value) == "Cannot withdraw more than is in the jar"
