# meal.py
# Aidan Linerud


def main():
    # Prompt the user for the time, and convert it to a numeric value
    user_input = input("What time is it? ")
    hours = convert(user_input)

    # Displays the meal time based on the current time
    if hours >= 7 and hours <= 8:
        print("breakfast time")
    elif hours >= 12 and hours <= 13:
        print("lunch time")
    elif hours >= 18 and hours <= 19:
        print("dinner time")


# Converts time as a string to time as a float
# (e.g. "9:30" is converted to 9.5)
def convert(time):
    hours, minutes = time.strip().split(":")
    hours = float(hours)
    # Convert minutes to hours
    decimal = float(minutes) / 60
    return hours + decimal


if __name__ == "__main__":
    main()
