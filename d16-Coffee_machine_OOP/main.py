from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_running = True
coffee_maker = CoffeeMaker()
menu = Menu()
coffee_menu = menu.get_items()
money_machine = MoneyMachine()

while machine_running:
    user_choice = input(f"What would you like? {coffee_menu}: ")

    if user_choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif user_choice == "off":
        machine_running = False
    else:
        choice = menu.find_drink(user_choice)
        if choice is not None and coffee_maker.is_resource_sufficient(choice) and money_machine.make_payment(choice.cost):
            coffee_maker.make_coffee(choice)
