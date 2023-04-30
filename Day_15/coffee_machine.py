#!//python3

"""This a virtual coffee machine"""
from coffe_machine_menu import MENU, resources
from coffee_machine_art import machine


def calculate_resources(resources, profit):
    """This prints out the resources when user prompts for report"""
    for keys, values in resources.items():
        if keys == "coffee":
            print("{}: {}g".format(keys, values))
            continue
        print("{}: {}ml".format(keys, values))
    print("Money: ${}".format(profit))


def resources_sufficient(user_order, resources):
    """This function returns the resources that is not sufficient"""
    for ingredeint, quantity in MENU[user_order]["ingredients"].items():
        if resources.get(ingredeint, 0) < quantity:
            print("There is not enough {}.".format(ingredeint))
            return False
        return True


def recalculate_resources(resources, user_order):
    """This function gets the recalculated resources"""
    for keys in MENU[user_order]["ingredients"]:
        if keys == "water":
            resources["water"] -= MENU[user_order]["ingredients"][keys]
        if keys == "milk":
            resources["milk"] -= MENU[user_order]["ingredients"][keys]
        if keys == "coffee":
            resources["coffee"] -= MENU[user_order]["ingredients"][keys]


def collect_coins(user_order):
    """This functions collects the coin and checks if it is enough"""
    while (True):
        try:
            print("Pls insert coins")
            quarter = float(input("How many quaters?: ")) * 0.25
            nickel = float(input("How many nickels?: ")) * 0.05
            dime = float(input("How many dimes?: ")) * 0.10
            penny = float(input("How many pennys?: ")) * 0.01

            # perform the calculations and check if it is sufficient
            money = quarter + nickel + dime + penny
            # check if the money is sufficient for the coffee
            coffee_money = MENU[user_order]["cost"]
            if coffee_money <= money:
                change = money - coffee_money
                print("Here is ${:.2f} in change".format(change))
                print("Here is your {} ☕. Enjoy!".format(user_order))
                break
            else:
                print("Money available is not enough")
                print("Money Refunded-------------------------------")
                return False
        except (ValueError, TypeError):
            print("Only coins accepted")


profit = 0  # profit global variable to keep track of the money made


def coffe_machine():
    """This is the code base for the coffee machine"""
    global profit
    print(machine)
    # ask user what they want
    while True:
        user_order = input("What would you like? "
                           "('espresso'/'latte'/'cappuccino'): ").lower()
        if user_order == "report":
            calculate_resources(resources, profit)
        elif user_order == "off":
            exit("switching off ________________")
        elif user_order in ["espresso", "latte", "cappuccino"]:
            if resources_sufficient(user_order, resources) == False:
                coffe_machine()
            elif collect_coins(user_order) == False:
                coffe_machine()
            recalculate_resources(resources, user_order)
            profit += MENU[user_order]["cost"]
        elif user_order not in ["espresso", "latte", "cappuccino"]:
            print("Invalid option")


coffe_machine()
