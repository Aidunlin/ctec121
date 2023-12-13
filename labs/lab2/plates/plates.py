def main():
    # Get input from the user
    plate = input("Plate: ")
    # Call the is_valid() function with the plate entered
    if is_valid(plate):
        # plate is valid since is_valid() returned True
        print("Valid")
    else:
        # plate is not valid since is_valid() returned False
        print("Invalid")


def is_valid(s):
    """
    s is the vanity plate that was passed in to the function
    within the is_valid() function it's now known as the variable s

    There are a lot of things that need be checked
    True can only be returned once we have gone through all of the checks that are in the lab assignment

    Start by checking to see if the length of s is less than 2 or greater than 6
    # if s is less than 2 or greater than 6 then False needs to be returned since it's not valid
    """

    if len(s) < 2 or len(s) > 6:
        return False

    """
    - All vanity plates must start with at least two letters
    - The first two characters of the vanity plate must be letters
    - There is a Python string method .isalpha() that can be used
    - Use string slicing to check both the first character, the one
    at position and 0 and the second character at position 1
    - The .isalpha() string method will return True if it's a letter from a-z
    - The .isalpha() string method will return False if it's not a letter from a-z
    """

    if not s[0:2].isalpha():
        return False

    """
    # Let's make sure all of the characters in the vanity plate are letters and/or numbers
    # This code will iterate through each character in the plate and check to make of this
    # for loops can be used to loop through, or iterate through character in a string
    """

    if not s.isalnum():
        return False

    """
    - Numbers cannot be used in the middle of a vanity plate. They must be at then end of a plate.
    - A vanity plate of BBB99 would be acceptable
    - A vanity plate of BB99A would not be acceptable
    - The first number must not be a 0
    - Let's a for loop to iterate through each character in the vanity plate
    - Note the use of the len() function within the range()

    - Declare a variable named firstNumber and set to True
    - This variable will be used to handle the logic for testing whether or not
    the first number we come across in the plate is in fact a 0
    """

    first_number = True
    for i in range(len(s)):
        if s[i].isdigit():
            if not s[i:].isdigit():
                return False
            if first_number and s[i] == "0":
                return False
            else:
                first_number = False


    # We made it through all of the checks above so we must now have a valid Vanity Plate
    return True


# Call the main() function to start the program
main()
