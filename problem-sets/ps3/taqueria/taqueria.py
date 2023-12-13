# PS 3 - Felipe's Taqueria
# Aidan Linerud

# Dictionary of entrees and their prices
menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}

# Total cost for all items inputted
cost = 0.0

# Repeatedly prompts user for entrees to add
while True:
    try:
        # Get user input
        item = input("Item: ").strip().title()

    # Stop prompting when user hits CTRL+D
    except EOFError:
        break

    # Add item's cost to total
    if item in menu:
        cost += menu[item]

    # Print current total
    print(f"Total: ${cost:.2f}")
