score = int(input("Enter quiz score (0-5): "))

if score < 2:
    print("F")
elif score < 3:
    print("D")
elif score < 4:
    print("C")
elif score < 5:
    print("B")
else:
    print("A")
