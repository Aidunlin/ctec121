# PS 2 - Coke Machine
# Aidan Linerud


due = 50
amount = 0

# Repeatedly asks for a coin value until the amount due is 0 or less
while amount < due:
    print(f"Amount Due: {due - amount}")

    coin = int(input("Insert Coin: "))
    if coin in 5, 10, 25:
        amount += int(coin)

print(f"Change Owed: {amount - due}")
