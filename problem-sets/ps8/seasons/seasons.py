# seasons.py
# Aidan Linerud

import datetime
import inflect
import re
import sys


def string_to_date(date_input: str) -> datetime.date:
    """
    Converts a date string (format: YYYY-MM-DD) to a date object
    """

    # Captures the year, month, and day from the input string
    date_match = re.match(r"^(\d{4})-(\d{2})-(\d{2})$", date_input)

    # Exits the program if year, month, and day could not be captured
    if not date_match:
        sys.exit("Invalid date")

    # Extracts the year, month, and day values from the capture groups
    match date_match.groups():
        case year, month, day:
            # Converts each value to integers
            year = int(year)
            month = int(month)
            day = int(day)
        case _:
            sys.exit("Invalid date")

    return datetime.date(year, month, day)


def minutes_between_dates(date1: datetime.date, date2: datetime.date) -> int:
    """
    Calculates the duration between two dates in minutes
    """

    # Gets the absolute value of change in time between the two dates
    delta = abs(date2 - date1)
    # Gets the total minutes of the change in time
    minutes = delta.total_seconds() / 60
    # Rounds to whole number
    return round(minutes)


def minutes_to_string(minutes: int) -> str:
    """
    Converts minutes to a string of words
    """

    # Creates an instance of inflect
    engine = inflect.engine()
    # Converts to words without using "and"
    minutes_words = engine.number_to_words(minutes, andword="")
    # Returns with the first letter capitalized
    return minutes_words.capitalize() + " minutes"


def main():
    """
    Prompts the user for their date of birth,
    calculates the total minutes between then and the current time,
    and prints out the minutes using English words
    """

    # Prompts the user for their date of birth
    birth_input = input("Date of Birth: ")

    # Calculates the total minutes between then and the current time
    birth_date = string_to_date(birth_input)
    today_date = datetime.date.today()
    minutes = minutes_between_dates(birth_date, today_date)
    
    # Prints out the minutes using English words
    print(minutes_to_string(minutes))


if __name__ == "__main__":
    main()
