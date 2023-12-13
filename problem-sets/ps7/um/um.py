# um.py
# Aidan Linerud

import re


# Returns the number of occurrences of the word "um" in a string
def count(string: str) -> int:
    return len(re.findall(r"\b(um)\b", string, re.IGNORECASE))


# Prints the number of occurrences of "um" from user input
def main():
    print(count(input("Text: ")))


if __name__ == "__main__":
    main()
