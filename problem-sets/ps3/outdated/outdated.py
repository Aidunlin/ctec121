# PS 3 - Outdated
# Aidan Linerud

# Ordered list of names of months
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

# Repeatedly prompt user for a date
while True:
    try:
        # Get user input
        date = input("Date: ").strip()

        # Checks if input format is like "Month D, Y"
        if " " in date and "," in date:
            # Remove comma after the day, split up input
            month, day, year = date.replace(",", "").split(" ")

            # Convert month name to integer
            month = months.index(month) + 1

        # Checks if input format is like "M/D/Y"
        elif "/" in date:
            # Split up input
            month, day, year = date.split("/")

            # Convert month to integer
            month = int(month)

        # Reprompt if user input is not either "Month D, Y" or "M/D/Y"
        else:
            continue

        # Convert rest of date to integers
        day = int(day)
        year = int(year)

        # Reprompt if month or day are invalid
        if month > 12 or day > 31:
            continue

        # Print date with ISO 8601 format
        print(f"{year:}-{month:02}-{day:02}")
        break

    # Reprompt if input has unknown month name or values are NaN
    except ValueError:
        pass
