from data import resources, MENU

total_money = 0
QUARTERS = 0.25
DIMES = 0.10
NICKLES = 0.05
PENNIES = 0.01

def display_report():
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}g')
    print(f'Money: ${total_money}')

def resource_required(coffee: str,money: int) -> bool:
    global total_money
    if money >= MENU[coffee]["cost"]:
        if money > MENU[coffee]["cost"]:
            change = round(money - MENU[coffee]["cost"],2)
            print(f"Here is the {change} in change")
        print(f"Here is your {coffee}☕. Enjoy!")
        total_money += money
        return True
    else:
        print("Sorry! that's not enough money. Money refunded")
        return False

def process_resources(coffee: str) -> bool:
    required_water = MENU[coffee]["ingredients"]["water"]
    required_coffee = MENU[coffee]["ingredients"]["coffee"]
    available_coffee = resources["coffee"]    
    available_water = resources["water"]

    if coffee != "espresso":
        required_milk = MENU[coffee]["ingredients"]["milk"]
        available_milk = resources["milk"]

    if coffee != "espresso" and available_milk < required_milk:
        print("​Sorry there is not enough milk.")
        return False
    elif available_water < required_water:
        print("Sorry there is not enough water.")
        return False
    elif available_coffee < required_coffee:
        print("​Sorry there is not enough coffee.")
        return False
    else:
        resources["water"] -= required_water
        resources["coffee"] -= required_coffee
        if coffee != "espresso":
            resources["milk"] -= required_milk
        return True

def process_coffee(coffee: str)-> None:
    if process_resources(coffee):
        print("Please insert coins. ")
        quarters = int(input("How many quarters? "))
        dimes = int(input("How many dimes? "))
        nickles = int(input("How many nikles? "))
        pennies = int(input("How many pennies? "))
        total_money_collected = quarters * QUARTERS + \
                                dimes * DIMES + \
                                nickles * NICKLES + \
                                pennies * PENNIES
        resource_required(coffee, total_money_collected)

condition_to_continue = True
while condition_to_continue == True:
    coffee_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if coffee_choice == "report":
        display_report()
    elif coffee_choice == "latte" or coffee_choice == "espresso" or coffee_choice ==  "cappuccino":
        process_coffee(coffee_choice)
    elif coffee_choice == "off":
        condition_to_continue = False