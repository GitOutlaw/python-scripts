MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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

# TODO: 1. User input asking the menu
# TODO: 2. Turning off for maintenance
# TODO: 3. Check resources using report
# TODO: 4. Check enough resources to make drink(s)


def menu_options():
    profit = 0
    running = True

    while running:

        menu = input("  What would you like? (espresso/latte/cappuccino): ")

        if menu == "off":
            running = False

        elif menu == "espresso":
            if resources["water"] > 50 and resources["coffee"] > 18:
                resources["water"] -= 50
                resources["coffee"] -= 18

                print("Please insert coins.")
                quarters = int(input("How many quarters?: "))
                dimes = int(input("How many dimes?: "))
                nickels = int(input("How many nickels?: "))
                pennies = int(input("How many pennies?: "))

                total_quarters = quarters * 0.25
                total_dimes = dimes * 0.10
                total_nickels = nickels * 0.05
                total_pennies = pennies * 0.01

                total_coins = total_quarters + total_dimes + total_nickels + total_pennies
                change = total_coins - MENU["espresso"]["cost"]
                
                profit += 1.50

                if total_coins >= 1.5:
                    print(f"Here us your change ${change}0")
                    print("Here is your espresso ☕. Enjoy!")

                else:
                    print("Sorry that's not enough money. Money refunded.")
            else:
                print("Sorry not enough resources")

        elif menu == "latte":
            if resources["water"] > 200 and resources["milk"] > 150 and resources["coffee"] >= 24:
                resources["water"] -= 200
                resources["milk"] -= 150
                resources["coffee"] -= 24

                print("Please insert coins.")
                quarters = int(input("How many quarters?: "))
                dimes = int(input("How many dimes?: "))
                nickels = int(input("How many nickels?: "))
                pennies = int(input("How many pennies?: "))

                total_quarters = quarters * 0.25
                total_dimes = dimes * 0.10
                total_nickels = nickels * 0.05
                total_pennies = pennies * 0.01

                total_coins = total_quarters + total_dimes + total_nickels + total_pennies
                change = total_coins - MENU["latte"]["cost"]
                profit += 2.50

                if total_coins >= 2.5:
                    print(f"Here us your change ${change}0")
                    print("Here is your latte ☕. Enjoy!")
                else:
                    print("Not enough money. Try again.")
            else:
                print("Sorry that's not enough money. Money refunded.")

        elif menu == "cappuccino":
            if resources["water"] > 250 and resources["milk"] > 100 and resources["coffee"] > 24:
                resources["water"] -= 250
                resources["milk"] -= 100
                resources["coffee"] -= 24

                print("Please insert coins.")
                quarters = int(input("How many quarters?: "))
                dimes = int(input("How many dimes?: "))
                nickels = int(input("How many nickels?: "))
                pennies = int(input("How many pennies?: "))

                total_quarters = quarters * 0.25
                total_dimes = dimes * 0.10
                total_nickels = nickels * 0.05
                total_pennies = pennies * 0.01

                total_coins = total_quarters + total_dimes + total_nickels + total_pennies
                change = total_coins - MENU["cappuccino"]["cost"]

                if total_coins >= 3.00:
                    print(f"Here us your change ${change}0.")
                    print("Here is your cappuccino ☕.")

                else:
                    print("Not enough money. Try again.")
            else:
                print("Sorry that's not enough money. Money refunded.")

        elif menu == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${profit}0")


menu_options()


# TODO: 5. Input coins by user


# def check_coins(check):
#     coin_check = total_coins


# TODO: 6. Calculate transaction

# TODO: 7. Add profit before making coffee
# TODO: 8-1. Make coffee deduct ingredients


# TODO: 8-2.  Print serving
# TODO: 10. serve the next customer by repeating from todo1
