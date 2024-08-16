
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
money=0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")

def check_resources(choice):
    ingredients=MENU[choice]["ingredients"]
    for i in ingredients:
        if ingredients[i]>resources[i]:
            print(f"Sorry there is not enough {i}.")
            return False
        return True

def process_coins():
    print("Please Insert Coins.")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickles = int(input("How many nickles?: ")) * 0.05
    pennis = int(input("How many dimes?: ")) * 0.1
    total = quarters + dimes + nickles + pennis
    return total

choice=input("What would you like? (espresso/latte/cappuccino): ").lower()
if choice =="off":
    print("Turning Off")
    exit()
if choice =="report":
    report()

#f=check_resources(choice)
#print(f)