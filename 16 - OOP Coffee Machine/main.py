import os
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from art import logo, priceboard

drink_menu = Menu()
coffee_ui = CoffeeMaker()
money_machine = MoneyMachine()

machine_on = True

print(logo)
print(priceboard)

while machine_on == True:
    user_choice = input(f"What would you like? ({drink_menu.get_items()[:-1]}): ")
    menu_choice = drink_menu.find_drink(user_choice)

    def process_order():
        money_machine.make_payment(menu_choice.cost)
        coffee_ui.make_coffee(menu_choice)

    def check_ingredients():
        if coffee_ui.is_resource_sufficient(menu_choice):
            process_order()

    if user_choice == "off":
        machine_on = False
    elif user_choice == "report":
        coffee_ui.report()
        money_machine.report()
    elif menu_choice != None:
        check_ingredients()

os.system("cls")
input("Press enter to exit...")