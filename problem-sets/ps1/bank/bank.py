# bank.py
# Aidan Linerud

# Obtain the bank's greeting (inputted by the user), and clean it up
greeting = input("Greeting: ")
greeting = greeting.strip().lower()

# Display the money the bank manager will give to Kramer, based on their greeting
if greeting.startswith("hello"):
    print("$0")
elif greeting.startswith("h"):
    print("$20")
else:
    print("$100")
