# working.py
# Aidan Linerud

# Did a bunch of refactoring!
# Reduced duplicate code and improved readability

import re


# Returns whether the minute was inputted and is valid,
# defaulting to True if it was not inputted
def minute_is_valid(minute) -> bool:
    if minute == None:
        # Minutes don't have to be included (e.g. 12 AM, 3 PM)
        return True
    else:
        return int(minute) < 59


# Converts a single time from 12-hour to 24-hour
def convert_12_to_24_hour(hour: str, minute: str, period: str) -> str:
    time_string = ""

    if period == "PM":
        # Converts PM hour to 24-hour
        if hour == "12":
            time_string = hour.zfill(2)
        else:
            time_string = str(int(hour) + 12).zfill(2)
    elif period == "AM":
        # Converts AM hour to 24-hour
        if hour == "12":
            # 12 AM = 00:00
            time_string = "00"
        else:
            time_string = hour.zfill(2)

    # Adds minute if inputted (or :00 otherwise)
    if minute != None:
        time_string += ":" + minute
    else:
        time_string += ":00"

    return time_string


# Converts a string of range of time from 12-hour to 24-hour
def convert(time_string: str) -> str:
    # Group 1 is the complete first time (i.e., 8:01 AM or 9:22 PM)
    # Group 2 is the first hour (i.e., 8)
    # Group 3 is the first minute (i.e., 01)
    # Group 4 is the first AM/PM (i.e., AM)
    # Group 5 is the second time (i.e., 9:22)
    # Group 6 is the second hour (i.e., 9)
    # Group 7 is the second minute (i.e., 22)
    # Group 8 is the second AM/PM (i.e., PM)
    time_match = re.search(
        r"^(([0-9]+):?([0-9]+)? ([AaPp][Mm])) to (([0-9]+):?([0-9]+)? ([AaPp][Mm]))$",
        time_string,
        re.IGNORECASE,
    )

    # Raises an error if the input doesn't follow the correct 12-hour format
    if time_match == None:
        raise ValueError

    first_hour = time_match.group(2)
    first_minute = time_match.group(3)
    first_period = time_match.group(4)
    second_hour = time_match.group(6)
    second_minute = time_match.group(7)
    second_period = time_match.group(8)

    # Raises an error if the first or second hour value is invalid
    if int(first_hour) > 12 or int(second_hour) > 12:
        raise ValueError

    # Raises an error if the first or second minute value is invalid
    # (either minute value can be left out, e.g. 11 AM to 4 PM)
    if not minute_is_valid(first_minute) or not minute_is_valid(second_minute):
        raise ValueError

    # Converts each inputted 12-hour time to its 24-hour form
    first_time = convert_12_to_24_hour(first_hour, first_minute, first_period)
    second_time = convert_12_to_24_hour(second_hour, second_minute, second_period)

    # Concatenates and returns the two parsed times together
    return first_time + " to " + second_time


def main():
    # Converts user-inputted hours from 12-hour format to 24-hour format
    print(convert(input("Hours: ").upper()))


if __name__ == "__main__":
    main()
