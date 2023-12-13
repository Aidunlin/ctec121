# PS-5 Back to the Bank
# Aidan Linerud


def main():
    greeting = input("Greeting: ")
    print(value(greeting))


# Displays the money the bank manager will give to Kramer, based on their greeting
def value(greeting: str) -> int:
    greeting = greeting.strip().lower()
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
