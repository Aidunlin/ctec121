# PS-5 Refueling
# Aidan Linerud


# Prompts the user for fuel amount as a fraction,
# then displays a fuel gauge for that amount
def main():
    while True:
        try:
            percent = convert(input("Fraction: "))
        except (ValueError, ZeroDivisionError):
            continue
        else:
            print(gauge(percent))
            break


# Converts a fraction to a percentage as an integer
def convert(fraction: str) -> int:
    fuel, _, max_fuel = fraction.strip().partition("/")

    # Converts to integers
    fuel = int(fuel)
    max_fuel = int(max_fuel)

    # Raises an error if values are unrealistic
    # (a fuel tank that can't hold any fuel,
    # or has more fuel than it can hold)
    if max_fuel == 0:
        raise ZeroDivisionError
    if fuel > max_fuel:
        raise ValueError

    # Converts to percentage as an integer
    return fuel / max_fuel * 100


# Creates a fuel gauge string from percentage as an integer
def gauge(percentage: int) -> str:
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{round(percentage)}%"


if __name__ == "__main__":
    main()
