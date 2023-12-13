# Midterm P1 - Word Check
# Aidan Linerud
# Loom video: https://www.loom.com/share/ee9f51e08bc64d6e852217de8d17954d

# Contains a sample of words and their definitions
# Top ten words taken from Wikipedia (https://en.wikipedia.org/wiki/Most_common_words_in_English)
# Definitions taken and simplified from Google dictionary boxes (https://support.google.com/websearch/answer/10106608?hl=en)
dictionary = {
    "the": "denoting someone or something",
    "be": "exist; occur; take place",
    "to": "expressing motion in the direction of",
    "of": "expressing the relationship between two entities",
    "and": "used to connect words, clauses, or sentences",
    "a": "used when referring to someone or something for the first time",
    "in": "expressing that something is enclosed by something else",
    "that": "used to identify a specific thing",
    "have": "possess; hold; experience",
    "i": "used to refer to oneself",
}


# Returns a sanitized, lowercased copy of a string
def cleanString(string: str) -> str:
    # Removes whitespace, converts to lowercase
    newString = string.strip().lower()

    # Converts the string to a list of characters, while only including letters and spaces
    characters = [char for char in newString if char.isalpha() or char == " "]

    # Join the character list into a string with an empty string ("") as the separator
    return "".join(characters)


# Returns a list of words from the given list if they don't appear in the given dictionary
def getMisspelledWords(words: list[str], dictionary: dict) -> list[str]:
    return [word for word in words if word not in dictionary]


# Displays a numbered list of misspelled words, and the total count of misspelled words
def displayResults(misspelledWords: list[str]):
    print("Incorrectly spelled words:")

    # Displays a numbered list of misspelled words
    for i, word in enumerate(misspelledWords):
        print(f"{i + 1}) {word}")

    print(f"Total incorrect words: {len(misspelledWords)}")


# Repeatedly prompts the user for sentences and displays any unknown/misspelled words
def main():
    while True:
        # Gets user input sentence
        try:
            sentence = input("Enter a sentence: ")

        # Breaks the loop if user hits CTRL+D or CTRL+C
        except (EOFError, KeyboardInterrupt):
            # Moves the terminal's cursor to a new line
            print()
            break

        # Sanitizes the user input, split up words into list
        words = cleanString(sentence).split(" ")

        # Creates a list of unknown/misspelled words using sample dictionary
        misspelledWords = getMisspelledWords(words, dictionary)

        # Displays the list
        displayResults(misspelledWords)


# Starts word check only if this file was run as a program
if __name__ == "__main__":
    main()
