# Currency converter. Pretty simple after doing the first API task. I didnt follow along with his tutorial,but I did steal his endpoint variables, as I could not find any documentation for python for this API.
# To use yourself, go to https://free.currencyconverterapi.com/ and sign up to get a free API key. Then paste it into the API_KEY constant and off you go.

from requests import get
from pprint import PrettyPrinter
import os

BASE_URL = "https://free.currconv.com/"
API_KEY = "(Personal API key)"

printer = PrettyPrinter()


def convert(first_info, second_info):
    os.system('cls')
    name1, symbol1, code1 = first_info["currencyName"], first_info["currencySymbol"], first_info["id"]
    symbol2, code2 = second_info["currencySymbol"], second_info["id"]

    endpoint = f"api/v7/convert?q={code1}_{code2}&compact=ultra&apiKey={API_KEY}"
    url = BASE_URL + endpoint
    exchange_rate = get(url).json()[f"{code1}_{code2}"]

    # Amount to exchange
    amount = input(f"How many {name1}s would you like to convert?   ") 
    while (not (amount.isnumeric) and int(amount) <= 0) or amount.lower() == "b":
        amount = input(f"How many {name1}s would you like to convert?   ")

    # Final output
    if amount.lower() != "b":
        os.system('cls')
        newamount = round(float(exchange_rate) * float(amount), 2)
        print(f"{symbol1}{amount} -----> {symbol2}{newamount}")
        print("Exchange rate:", exchange_rate, "\n")
        smth = input("\nPress any key to continue...")


def get_inputs():
    endpoint = f"api/v7/currencies?apiKey={API_KEY}"
    url = BASE_URL + endpoint
    data = get(url).json()

    # List of all acceptable codes
    codes = []
    for currency in data["results"]:
        codes.append(currency)
    
    first, second = "a", "a"
    while first.upper() not in codes and first.lower() != "b":
        os.system('cls')
        print("Which currency would you like to convert from?")
        first = input("Enter the currency code here:   ")

    if first.lower() != "b":
        while second.upper() not in codes and second.lower() != "b":
            os.system('cls')
            print("Which currency would you like to convert to?")
            second = input("Enter the currency code here:   ")

        if second.lower() != "b":
            # Info: Name, Symbol, Code
            first_info = data["results"][first.upper()]
            second_info = data["results"][second.upper()]

            convert(first_info, second_info)


def get_currencies():
    endpoint = f"api/v7/currencies?apiKey={API_KEY}"
    url = BASE_URL + endpoint
    data = get(url).json()

    count = 1

    # Prints each currency along with it's info
    for code in data["results"]:
        name = data["results"][code]["currencyName"]
        printer.pprint(f"{count}. {code} - {name}")
        count += 1

    smth = input("\nPress any key to continue...")


if __name__ == "__main__":
    done = False
    while not done:
        # Main menu
        os.system('cls')
        print("Welcome to the currency converter.")
        print("Enter b to go back to the main menu at any time.\n")
        print("1. Find conversion rate")
        print("2. Find currency codes")
        print("3. Quit\n")

        choice = "a"
        while choice not in ["1", "2", "3"]:
            choice = input("What would you like to do today?   ")

        if choice == "1":
            get_inputs()

        elif choice == "2":
            get_currencies()

        elif choice == "3":
            done = True

