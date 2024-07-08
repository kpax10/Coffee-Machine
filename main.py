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
    "money": 0,
}


# Print report of all coffee machine resources
def print_resources(resources):
    print("Water:", resources['water'])
    print("Milk:", resources['milk'])
    print("Coffee:", resources['coffee'])
    print("Money:", resources['money'])


def check_resources(user_input, MENU, resources):
    # loop over menu
    for drink in MENU:
        if user_input == drink:
            drink_ingredients = MENU[drink]['ingredients']
            for ingredient in drink_ingredients:
                if resources[ingredient] - drink_ingredients[ingredient] <= 0:
                    print(f"Sorry, there is not enough {ingredient}")
                    break
                else:
                    resources[ingredient] -= drink_ingredients[ingredient]
                    # run function to request payment


is_still_running = True

while is_still_running:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_input == 'report':
        print_resources(resources)
    if user_input == 'off':
        break

    check = check_resources(user_input, MENU, resources)


# TODO: 5. Display cost.

# TODO: 6.Process coins.
#   a. If there are sufficient resources to make the drink selected, then the program should
#       prompt the user to insert coins.
#   b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
#   c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
#      pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52

# TODO: 7. Check transaction successful?
#   a. Check that the user has inserted enough money to purchase the drink they selected.
#       E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
#       program should say “Sorry that's not enough money. Money refunded.”
#   b. But if the user has inserted enough money, then the cost of the drink gets added to the
#       machine as the profit and this will be reflected the next time “report” is triggered. E.g.
#       Water: 100ml
#       Milk: 50ml
#       Coffee: 76g
#       Money: $2.5
#   c. If the user has inserted too much money, the machine should offer change.E.g. “Here is
#       $2.45 dollars in change.” The change should be rounded to 2 decimal places.

# TODO: 8. Make Coffee.
#   a. If the transaction is successful and there are enough resources to make the drink the
#       user selected, then the ingredients to make the drink should be deducted from the
#       coffee machine resources.
#   b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
#       latte was their choice of drink.