# test_working.py
# Aidan Linerud

from working import convert
import pytest


# Checks if 12-hour times are correctly converted to 24-hour times
def test_convert_correct_time():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"


# Checks that an invalid hour input raises an error
def test_convert_incorrect_hours():
    with pytest.raises(ValueError):
        convert("23 AM to 8 PM")


# Checks that an invalid minute input raises an error
def test_convert_incorrect_minutes():
    with pytest.raises(ValueError):
        convert("12:99 AM to 5 PM")


# Checks that an error is raised if "to" is missing
def test_convert_no_to():
    with pytest.raises(ValueError):
        convert("11 AM 9 PM")


# Checks that an error is raised if an AM/PM is missing
def test_convert_invalid_time_format():
    with pytest.raises(ValueError):
        convert("8 AM to 12")
