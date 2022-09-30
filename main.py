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


def report():
    print(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: "
          f"{resources['coffee']}\nMoney: ${money}")


def process(drink):
    if drink == "espresso":
        if MENU[drink]["ingredients"]["water"] > resources["water"]:
            print("Sorry, there is not enough water")
            return False
        elif MENU[drink]["ingredients"]["coffee"] > resources["coffee"]:
            print("Sorry, there is not enough coffee")
            return False
        else:
            resources["water"] = resources["water"] - MENU[drink]["ingredients"]["water"]
            resources["coffee"] = resources["coffee"] - MENU[drink]["ingredients"]["coffee"]
            return True
    else:
        if MENU[drink]["ingredients"]["water"] > resources["water"]:
            print("Sorry, there is not enough water")
            return False
        elif MENU[drink]["ingredients"]["milk"] > resources["milk"]:
            print("Sorry, there is not enough milk")
            return False
        elif MENU[drink]["ingredients"]["coffee"] > resources["coffee"]:
            print("Sorry, there is not enough coffee")
            return False
        else:
            return True


def make(drink):
    if drink == "espresso":
        resources["water"] -= MENU[drink]["ingredients"]["water"]
        resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
    else:
        resources["water"] -= MENU[drink]["ingredients"]["water"]
        resources["milk"] -= MENU[drink]["ingredients"]["milk"]
        resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]


def calculate(quarters, dimes, nickels, pennies):
    total = 0
    total += quarters * .25
    total += dimes * .1
    total += nickels * .05
    total += pennies * .01
    return total


money = 0
checker = ""
while checker != "off":
    option = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if option == "report":
        report()
    elif option == "off":
        checker = "off"
    elif option not in MENU:
        print("Invalid option, please go again")
    else:
        if process(option):
            print("Please insert coins.")
            amount = calculate(int(input("How many quarters?")), int(input("How many dimes?")),
                               int(input("How many nickels?")), int(input("How many pennies?")))
            if amount < MENU[option]['cost']:
                print("Sorry, that's not enough money. Money refunded")
            else:
                money += MENU[option]['cost']
                print(f"Here is ${amount - MENU[option]['cost']} in change.")
                make(option)
                print(f"Here is your {option}. Enjoy!")
