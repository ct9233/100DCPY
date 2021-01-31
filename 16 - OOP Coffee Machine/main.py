import os
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from art import logo, priceboard

drink_menu = Menu()
coffee_ui = CoffeeMaker()
machine_on = True

print(logo)
print(priceboard)

while machine_on == True:
    user_choice = input(f"What would you like? ({drink_menu.get_items()[:-1]}): ")

    def check_ingredients():
        if coffee_ui.is_resource_sufficient(user_choice):
            process_order()
        else:
            print("There are insufficient ingredients to make that order.")

    if user_choice == "off":
        machine_on = False
    elif user_choice == "report":
        print(coffee_ui.report())
    elif drink_menu.find_drink(user_choice) != "None":
        check_ingredients()

os.system("cls")
input("Press enter to exit...")