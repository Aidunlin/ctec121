# PS 3 - Grocery List
# Aidan Linerud

# User's grocery list
# key: grocery name, value: grocery count
groceries = {
    # example: "APPLE": 3,
}

# Repeatedly prompts the user to add a grocery item to the list
while True:
    try:
        # Get user input
        grocery = input().upper()

        # If grocery input already exists in list, increment that grocery's count
        if grocery in groceries:
            groceries[grocery] += 1

        # Otherwise create a new entry
        else:
            groceries[grocery] = 1

    # Stop prompting when user hits CTRL+D
    except EOFError:
        # Blank line for padding
        print()

        # Print out each grocery and its count alphabetically
        for grocery in sorted(groceries):
            print(f"{groceries[grocery]} {grocery}")

        break
