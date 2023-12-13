# PS 4 - Guessing Game
# Aidan Linerud

from random import randint


# Repeatedly prompts the user to input upper bound for random answer
def get_level() -> int:
    while True:
        # Gets upper bound from user, reprompts if it's not an integer
        try:
            level = int(input("Level: "))
        except ValueError:
            continue

        # Accepts only positive integers
        if level > 0:
            return level


# Creates a random number between 1 and the user's requested level
def create_answer(level: int) -> int:
    return randint(1, level)


# Repeatedly prompts the user to guess the answer until guess is correct
def guess(answer: int):
    while True:
        # Gets user's guess, reprompts if it's not an integer
        try:
            guess = int(input("Guess: "))
        except ValueError:
            continue

        # Responds to user's guess, breaks if guess is correct
        if guess == answer:
            print("Just right!")
            break
        elif guess < answer:
            print("Too small!")
        elif guess > answer:
            print("Too large!")


# Gets user level, creates random answer from it, and prompts the user to guess random number
def main():
    level = get_level()
    answer = create_answer(level)
    guess(answer)


# Runs code when this file is run as a program
if __name__ == "__main__":
    main()
