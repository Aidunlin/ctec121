# PS-5 Back to the Bank
# Aidan Linerud

from bank import value


# Catches bank.py with incorrect values
def test_bank_has_correct_values():
    assert value("hello") == 0
    assert value("hi") == 20
    assert value("goodbye") == 100


# Catches bank.py without case-insensitivity
def test_bank_is_case_insensitive():
    assert value("HELLO") == 0
    assert value("HI") == 20


# Catches bank.py not allowing for entire phrase
def test_bank_allows_entire_phrase():
    assert value("Hello there") == 0
    assert value("General Kenobi") == 100
