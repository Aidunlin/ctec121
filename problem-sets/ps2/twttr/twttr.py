# PS 2 - Just setting up my twttr
# Aidan Linerud

# Set up user input and output
text = input("Input: ").strip()
output = ""

# Loop through every character in user input
for char in text:
    # Filter out vowels
    if not char.lower() in "aeiou":
        output += char

print(f"Output: {output}")
