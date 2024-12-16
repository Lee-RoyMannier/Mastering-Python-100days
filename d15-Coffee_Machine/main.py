def report():
    unite = "ml"
    for item, value in resources.items():
        if item == "Coffee":
            unite = "g"
        print(f"{item}: {value}{unite}")
    print(f"{"Money"}: {money}¥")


def is_sufficent_ressource(coffee_name):
    coffee = MENU[coffee_name.lower()]
    for ingredient, value in coffee["ingredients"].items():
        if resources[ingredient] < value:
            print("Sorry there is not enought ", ingredient)
            return False
    return True


def get_money():
    total = 0
    money = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    for item in money:
        total += int(input(f"How many {item}?")) * money[item]

    return total


def successful_transaction(money, coffee):
    return money >= MENU[coffee]["cost"]


def get_difference(money, coffee):
    return money - MENU[coffee]["cost"]


def make_coffee(coffee):
    for ingredient, value in MENU[coffee]["ingredients"].items():
        resources[ingredient] -= value
    print("Enjoy")


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = 0

running_machine = True

while running_machine:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")

    if user_choice == "off":
        running_machine = False
    elif user_choice == "report":
        report()
    elif user_choice not in MENU.keys():
        print("This coffee don't exist")
    else:
        is_sufficent_r = is_sufficent_ressource(user_choice)
        if is_sufficent_ressource:
            coffee_cost = get_money()

            if successful_transaction(coffee_cost, user_choice):
                money += coffee_cost
                to_change = get_difference(coffee_cost, user_choice)
                print("Here your ¥", to_change)
                money -= to_change
                make_coffee(user_choice)
