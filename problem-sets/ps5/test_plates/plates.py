# PS-5 Re-requesting Vanity Plates
# Aidan Linerud


# Checks if user-inputted vanity plate is valid
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


# Determines if a vanity plate follows the requirements
def is_valid(plate: str) -> bool:
    # Checks for correct length
    if len(plate) < 2 or len(plate) > 6:
        return False

    # Checks for first two letters
    if not plate[0:2].isalpha():
        return False

    # Checks for only alphanumeric characters
    if not plate.isalnum():
        return False

    first_number = True
    for i in range(len(plate)):
        if plate[i].isdigit():
            # Checks for no letters after this number
            if not plate[i:].isdigit():
                return False

            # Checks for 0 not being the first letter
            if first_number and plate[i] == "0":
                return False
            else:
                first_number = False

    return True


if __name__ == "__main__":
    main()
