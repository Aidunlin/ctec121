# test_jar.py
# Aidan Linerud

from jar import Jar
import pytest


def test_init():
    cookies = 7
    jar = Jar(cookies)
    assert jar.capacity == cookies


def test_str():
    jar = Jar()
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"


def test_deposit():
    cookies = 5
    jar = Jar()
    jar.deposit(cookies)
    assert jar.size == cookies


def test_withdraw():
    cookies_made = 7
    cookies_eaten = 3

    jar1 = Jar()
    jar1.deposit(cookies_made)
    jar1.withdraw(cookies_eaten)

    assert jar1.size == cookies_made - cookies_eaten

    with pytest.raises(ValueError):
        jar2 = Jar()
        jar2.deposit(4)
        jar2.withdraw(6)
