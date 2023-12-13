"""
CTEC 121
Lab 3
This program will convert a temperature entered in Celsius to Fahrenheit
"""


def temp_converter():
    # ask the person how many temperature conversion they want to calculate
    # store the number in the variable numberOfIterations
    numberOfIterations = int(input('How many temperature conversions would you like to perform? '))

    # Using the variable numberOfIterations perform a counted loop
    # Notice how the variable numberOfIterations is used within the range() function
    for i in range(numberOfIterations):
        # Ask the person to enter temperature in Celsius and convert it to an integer (whole number)
        # Store the Celsius temperature in a variable named celsius
        celsius = int(input('Enter temperature in Celsius: '))
        # Convert the temperature to Fahrenheit using the expression to the right of the = sign
        # Store the converted temperature in a variable named fahrenheit
        fahrenheit = 9/5 * celsius + 32
        # Display the Celsius and Fahrenheit temperatures to the person
        print(celsius, 'Celsius is', fahrenheit, 'in Fahrenheit.')


# Call the temp_converter function which will start the program
temp_converter()
