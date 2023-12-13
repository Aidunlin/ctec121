# deep.py
# Aidan Linerud

# Ask the Most Important Question, and clean the user's answer to the question
user_answer = input(
    "What is the Answer to the Great Question of Life, the Universe, and Everything? ")
user_answer = user_answer.strip().lower()

# Respond yes or no if the user answered (objectively) correctly
if user_answer == "42" or user_answer == "forty-two" or user_answer == "forty two":
    print("Yes")
else:
    print("No")
