# PS-5 Re-requesting Vanity Plates
# Aidan Linerud

from plates import is_valid


# Catches plates.py without beginning alphabetical checks
def test_plates_checks_beginning_alpha():
    assert is_valid("CS50")
    assert not is_valid("50")


# Catches plates.py without length checks
def test_plates_has_length_checks():
    assert not is_valid("S")
    assert not is_valid("BIGPLATE")


# Catches plates.py without checks for number placement
def test_plates_checks_number_placement():
    assert not is_valid("CS50CS")


# Catches plates.py without checks for zero placement
def test_plates_checks_zero_placement():
    assert not is_valid("CS05")


# Catches plates.py without checks for alphanum characters
def test_plates_checks_alphanum_characters():
    assert not is_valid("CS.50")
    assert not is_valid("CS 50")
    assert not is_valid("CS!50")
