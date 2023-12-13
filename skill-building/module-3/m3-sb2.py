def main():
    apr = float(input("What is the annual interest rate? "))
    principal = 1
    years = 0

    while principal < 2:
        principal *= 1 + apr
        years += 1

    print(f"Years to double: {years}")


main()
