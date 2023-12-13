# PS-5 Testing my twttr
# Aidan Linerud


def main():
    text = input("Input: ").strip()
    output = shorten(text)
    print(f"Output: {output}")


# Returns a copy of word with vowels removed
def shorten(word: str) -> str:
    output = ""

    # Loops through every character in word
    for char in word:
        # Adds character to output if it's not a vowel
        if not char.lower() in "aeiou":
            output += char

    return output


if __name__ == "__main__":
    main()
