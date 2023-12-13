# interpreter.py
# Aidan Linerud

# Get an arithmetic expression from the user, and parse it
expression = input("Expression: ").strip()
a, operator, b = expression.split(" ")

# Ensure we can do math
a = int(a)
b = int(b)

# Evaluate and display the expression
match operator:
    case "+":
        print(f"{(a + b):.1f}")
    case "-":
        print(f"{(a - b):.1f}")
    case "*":
        print(f"{(a * b):.1f}")
    case "/":
        print(f"{(a / b):.1f}")
