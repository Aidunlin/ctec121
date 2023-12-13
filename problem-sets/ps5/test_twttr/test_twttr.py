# PS-5 Testing my twttr
# Aidan Linerud

from twttr import shorten


# Catches twttr.py without capitalized vowel replacement
def test_twttr_removes_uppercase_vowels():
    assert shorten("AEIOU") == ""


# Catches twttr.py without lowercase vowel replacement
def test_twttr_removes_lowercase_vowels():
    assert shorten("aeiou") == ""


# Catches twttr.py omitting numbers
def test_twttr_keeps_numbers():
    assert shorten("12345") == "12345"


# Catches twttr.py printing in uppercase
def test_twttr_maintains_case():
    assert shorten("bCdFgHjK") == "bCdFgHjK"


# Catches twttr.py omitting punctuation
def test_twttr_keeps_punctuation():
    assert shorten(",.!?:;") == ",.!?:;"
