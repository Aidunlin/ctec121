# PS 4 - Emojize
# Aidan Linerud

# Imports emojize function
from emoji import emojize

# Gets user input
string = input("Input: ")

# Replaces emoji names with emojis
output = emojize(string)

# Displays output
print(f"Output: {output}")
