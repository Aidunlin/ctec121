# test_numb3rs.py
# Aidan Linerud

from numb3rs import validate


# Catches numb3rs.py only checking first byte of IPv4 address
# (The CS50 check for this unit test seems to be borked)
def test_numb3rs_checks_bytes_other_than_first():
    assert validate("1.1.1.1000") == False
    assert validate("1.1.1000.1") == False
    assert validate("1.1000.1.1") == False
    assert validate("1000.1.1.1") == False


# Catches numb3rs.py failing to return False for invalid IPv4 format
def test_numb3rs_returns_false_for_invalid_format():
    assert validate("127:0:0:1") == False
    assert validate("Pizza.Fries.Shake.Donut") == False


# Catches numb3rs.py accepting five-byte addresses
def test_numb3rs_rejects_five_byte_addresses():
    assert validate("127.0.0.0.1") == False
