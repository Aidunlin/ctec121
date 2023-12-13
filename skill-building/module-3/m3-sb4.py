def main():
    score = int(input("Enter the score (out of 100): "))
    grades = 60 * "F" + 10 * "D" + 10 * "C" + 10 * "B" + 11 * "A"
    print(f"The grade is {grades[score]}")


main()
