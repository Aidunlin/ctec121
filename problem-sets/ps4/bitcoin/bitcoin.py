# PS 4 - Bitcoin Price Index
# Aidan Linerud

import sys
import requests


# Converts a user-inputted bitcoin amount to USD using Coindesk's API
def main():
    # Attempts to get user-inputted command-line argument
    try:
        bitcoins = sys.argv[1]
    except IndexError:
        sys.exit("Missing command-line argument")

    # Attempts to convert the command-line argument to a float
    try:
        bitcoins = float(bitcoins)
    except ValueError:
        sys.exit("Command-line argument is not a number")

    # Attempts to request information from Coindesk API
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    except requests.RequestException:
        sys.exit("Failed to get response from Coindesk API")

    # Attempts to get the bitcoin-to-USD rate from the response
    try:
        rate = response.json()["bpi"]["USD"]["rate_float"]
    except KeyError:
        sys.exit("Could not find bitcoin price from response")

    # Calculates and prints the cost (in USD) of inputted bitcoins
    cost = bitcoins * rate
    print(f"${cost:,.4f}")


if __name__ == "__main__":
    main()
