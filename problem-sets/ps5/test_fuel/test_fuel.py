# PS-5 Refueling
# Aidan Linerud

import pytest
from fuel import convert, gauge


# Catches fuel.py returning incorrect ints in convert
def test_fuel_convert_returns_correct_ints():
    assert convert("0/4") == 0
    assert convert("1/4") == 25
    assert convert("2/4") == 50
    assert convert("3/4") == 75
    assert convert("4/4") == 100


# Catches fuel.py not raising ValueError in convert
def test_fuel_convert_raises_value_error():
    with pytest.raises(ValueError) as excinfo:
        convert("a/b")
        convert("4/3")


# Catches fuel.py not raising ZeroDivisionError in convert
def test_fuel_convert_raises_zero_division_error():
    with pytest.raises(ZeroDivisionError) as excinfo:
        convert("1/0")


# Catches fuel.py not labeling 1% as E in gauge
def test_fuel_gauge_labels_1_percent():
    assert gauge(1) == "E"


# Catches fuel.py not printing % in gauge
def test_fuel_gauge_prints_percent_symbol():
    assert gauge(50).endswith("%")


# Catches fuel.py not labeling 99% as F in gauge
def test_fuel_gauge_labels_99_percent():
    assert gauge(99) == "F"
