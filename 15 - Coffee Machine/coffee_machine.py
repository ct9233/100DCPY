import os
from art import logo, priceboard
from menu import MENU

machine_on = True
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

print(logo)
print(priceboard)

while machine_on == True:

    user_choice = input("What would you like? (espresso/latte/cappuccino): ")

    def process_order():
        print("Please insert coins.")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickels = int(input("How many nickels?: "))
        pennies = int(input("How many pennies?: "))

        total_paid = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)

        if eval("MENU['" + user_choice + "']['cost']") > total_paid:
            print("Sorry that's not enough money. Money refunded.")
        else:
            refund = round(total_paid - eval("MENU['" + user_choice + "']['cost']"), 2)
            print(f"\nHere is ${refund} in change.")
            for k in resources:
                try:
                    eval("MENU['" + user_choice + "']['ingredients']['" + k + "']")
                except KeyError:
                    continue
                else:
                    resources[k] -= eval("MENU['" + user_choice + "']['ingredients']['" + k + "']")
            if 'money' in resources:
                resources['money'] += eval("MENU['" + user_choice + "']['cost']")
            else:
                resources['money'] = eval("MENU['" + user_choice + "']['cost']")
            print(f"Here is your {user_choice}. Enjoy!\n")

    def check_ingredients():
        choice_ingredients = "MENU['" + user_choice + "']['ingredients']"

        if eval(choice_ingredients + "['water']") > resources["water"]:
            print("Sorry there is not enough water.")
            return
        if (
            "['" + user_choice + "']['ingredients']['milk']" in MENU
            and eval(choice_ingredients + "['milk']") > resources["milk"]
        ):
            print("Sorry there is not enough milk.")
            return
        if eval(choice_ingredients + "['coffee']") > resources["coffee"]:
            print("Sorry there is not enough coffee.")
            return
        else:
            process_order()

    if user_choice == "off":
        machine_on = False
    elif user_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        if 'money' in resources:
            print(f"Money: ${resources['money']}")
    elif user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
        check_ingredients()


os.system("cls")
input("Press enter to exit...")