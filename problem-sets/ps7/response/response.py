# response.py
# Aidan Linerud

import validators

# Displays whether user input is a valid email address
if validators.email(input("What's your email address? ")):
    print("Valid")
else:
    print("Invalid")
