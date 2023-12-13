# PS 2 - camelCase
# Aidan Linerud

# Set up user input and output
camel_name = input("Enter a variable name in camelCase: ").strip()
snake_name = ""

# Accumulate output string from input (without mutating input)
for char in camel_name:
    # Underscore goes before next word
    if char.isupper():
        snake_name += "_"
    snake_name += char.lower()

print(snake_name)

# TODO: Run this program in itself
