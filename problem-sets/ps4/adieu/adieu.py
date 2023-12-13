# PS 4 - Adieu, Adieu
# Aidan Linerud

import inflect


p = inflect.engine()


# Prompts the user for a list of names and bids adieu
def main():
    # Stores a list of user-inputted names
    names = []

    # Repeatedly prompts user for names, stopping when they hit CTRL+D
    while True:
        try:
            name = input("Name: ")
        except EOFError:
            break

        names.append(name)

    # Bids adieu to every inputted name using correct English
    print()
    print(f"Adieu, adieu, to {p.join(names)}")


if __name__ == "__main__":
    main()
