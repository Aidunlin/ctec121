# CTEC 121
# Lab 4
# IMPORTANT: There is nothing that you need to modify in this code
# IMPORTANT: Please follow the directions outlined in the Canvas assignment


def sumNumbersInList():
    accumulator = 0
    grades = [88, 99, 100, 65, 75, 20, 100, 99, 75, 77, 84]  # list of grades
    for grade in grades:  # loop through each grade in the list
        accumulator = accumulator + grade  # accumulate sum of grades
    print("The average grade is", round(accumulator / len(grades), 2))


sumNumbersInList()
