# for staffs only:
# #"report" : it shows how much resources are left and how much money is added
# #"off" : it offs the machine

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
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


def resources_sufficient(coffee_type):
    water = MENU[coffee_type]["ingredients"]["water"]
    milk = MENU[coffee_type]["ingredients"]["milk"]
    coffee = MENU[coffee_type]["ingredients"]["coffee"]
    if resources["water"] < water:
        print("Sorry there is not enough water.")
    elif resources["milk"] < milk:
        print("Sorry there is not enough milk.")
    elif resources["coffee"] < coffee:
        print("Sorry there is not enough coffee.")
    else:
        process_coins(coffee_type)


def process_coins(coffee_type):
    cost = MENU[coffee_type]["cost"]
    print("Please enter coins.")
    quarters = int(input("how many quarters: "))
    dimes = int(input("how many dimes: "))
    nickles = int(input("how many nickles: "))
    pennies = int(input("how many pennies: "))
    entered_amount = (0.25*quarters) + (0.10*dimes) + (0.05*nickles) + (0.01*pennies)
    if cost > entered_amount:
        print("Sorry that's not enough money. Money refunded.")
    else:
        if cost < entered_amount:
            change = round(entered_amount - cost, 2)
            print(f"Here is ${change} in change.")
        print(f"Here is your {coffee_type}.Enjoy")
        updating_resource(coffee_type)


def updating_resource(coffee_type):
    water = MENU[coffee_type]["ingredients"]["water"]
    milk = MENU[coffee_type]["ingredients"]["milk"]
    coffee = MENU[coffee_type]["ingredients"]["coffee"]
    resources["water"] -= water
    resources["milk"] -= milk
    resources["coffee"] -= coffee
    global MONEY
    MONEY += MENU[coffee_type]["cost"]


MONEY = 0
on = True
while on:
    type_of_coffee = input("What would you like? (espresso/latte/cappuccino) ").lower()
    if type_of_coffee == "espresso":
        resources_sufficient("espresso")
    elif type_of_coffee == "latte":
        resources_sufficient("latte")
    elif type_of_coffee == "cappuccino":
        resources_sufficient("cappuccino")
    elif type_of_coffee == "report":
        print(f"water: {resources['water']}ml\nmilk: {resources['milk']}ml\ncoffee: {resources['coffee']}g\n"
              f"Money: ${MONEY}")
    elif type_of_coffee == "off":
        on = False
    else:
        print("Invalid type of coffee.")
