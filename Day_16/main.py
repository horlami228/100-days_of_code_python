from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

""" We have to create a coffee object """
menu = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    options = menu.get_items()
    user_choice = input("What do you want? ({}): ".format(options)).lower()
    if user_choice == "report":
        coffee_machine.report()
        money_machine.report()
    elif user_choice == "off":
        break
    else:
        drink = menu.find_drink(user_choice)
        if coffee_machine.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_machine.make_coffee(drink)





