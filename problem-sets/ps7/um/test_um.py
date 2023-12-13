# test_um.py
# Aidan Linerud

import um


# Catches um.py matching "um" in words
def test_um_ignores_um_in_words():
    assert um.count("bummer") == 0


# Catches um.py with regular expression requiring spaces around "um"
def test_um_matches_single_um():
    assert um.count("um") == 1


# Catches um.py without case-insensitive matching of "um"
def test_um_ignores_case():
    assert um.count("um UM uM Um") == 4
