from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

total_money_collected = 0
my_coffee_maker = CoffeeMaker()
my_menu = Menu()
my_money_machine = MoneyMachine()

condition_to_continue = True
while condition_to_continue == True:
    options = my_menu.get_items()
    coffee_choice = input(f"What would you like? ({options}): ")
    if coffee_choice == "report":
        my_coffee_maker.report()
        my_money_machine.report()
    elif coffee_choice == "latte" or coffee_choice == "espresso" or coffee_choice ==  "cappuccino":
        drink = my_menu.find_drink(coffee_choice)
        if my_coffee_maker.is_resource_sufficient(drink) and my_money_machine.make_payment(drink.cost):
            my_coffee_maker.make_coffee(my_menu.find_drink(coffee_choice))
    elif coffee_choice == "off":
        condition_to_continue = False