# numb3rs.py
# Aidan Linerud


# Returns whether an IPv4 address is valid
def validate(ip: str) -> bool:
    # Converts the address to a list of strings
    ip = ip.split(".")

    # IPv4 addresses must have exactly 4 values
    if len(ip) != 4:
        return False

    # Checks if each value is valid
    for value in ip:
        # The value must be a number...
        if not value.isdigit():
            return False

        # ... and it must be between 0 and 255
        number = int(value)
        if number < 0 or number > 255:
            return False

    # All checks passed, the IP address is valid
    return True


def main():
    # Displays whether a user-inputted IP address is valid
    print(validate(input("IPv4 Address: ")))


if __name__ == "__main__":
    main()
