# PS 4 - Frank, Ian and Glen's Letters
# Aidan Linerud

import random
import sys
from pyfiglet import Figlet

# Creates figlet object
figlet = Figlet()

# Matches the structure of command-line args,
# either setting the figlet's font or exiting the program
match sys.argv:
    # No args provided
    case [_]:
        # Sets a random default font
        font_name = random.choice(figlet.getFonts())
        figlet.setFont(font=font_name)

    # Two args provided, where the first must be a font flag
    case [_, ("-f" | "--font"), font_name]:
        # Exits if first argument is not a flag or second argument is not a font
        if font_name not in figlet.getFonts():
            sys.exit("Invalid usage")

        # Sets the font to the second argument
        figlet.setFont(font=font_name)

    # Catch-all for unsupported font flags or too many args
    case _:
        sys.exit("Invalid usage")

# Finally, gets user input and renders it as beautiful ASCII art
user_input = input("Input: ")
print(figlet.renderText(user_input))
