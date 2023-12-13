# PS 3 - Fuel Gauge
# Aidan Linerud

# Repeatedly prompts user for fuel gauge
while True:
    try:
        # Get user input
        x, _, y = input("Fraction: ").strip().partition("/")

        # Convert to integers
        x = int(x)
        y = int(y)

        # Reprompt if x/y is greater than 1
        if x > y:
            continue

        # Calculate fuel gauge percent
        a = x / y * 100

        # Display fuel gauge
        if a <= 1:
            print("E")
        elif a >= 99:
            print("F")
        else:
            print(f"{round(a)}%")

        # Stop prompting user
        break

    # Reprompt if user entered invalid value or divided by zero
    except (ValueError, ZeroDivisionError):
        pass
