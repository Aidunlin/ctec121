# test_seasons.py
# Aidan Linerud

from datetime import date
import seasons


# Catches seasons.py incorrectly parsing time string
def test_seasons_string_to_date():
    assert seasons.string_to_date("2000-01-01") == date(2000, 1, 1)


# Catches seasons.py incorrectly calculating the time between two dates
def test_seasons_minutes_between_dates():
    assert seasons.minutes_between_dates(date(2000, 1, 1), date(2000, 1, 2)) == 1440


# Catches seasons.py incorrectly converting minutes to English words
def test_seasons_minutes_to_string():
    assert seasons.minutes_to_string(1440) == "One thousand, four hundred forty minutes"
