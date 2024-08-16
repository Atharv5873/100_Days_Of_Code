
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
global money
money = 0
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

def process_coins(choice):
    bill=MENU[choice]["cost"]
    print(f"Your Total Bill is: {bill}")
    print("Please Insert Coins.")
    total=0
    total += int(input("How many quarters?: ")) * 0.25
    print(f"Your Have Given: {total}")
    total += int(input("How many dimes?: ")) * 0.10
    print(f"Your Have Given: {total}")
    total += int(input("How many nickles?: ")) * 0.05
    print(f"Your Have Given: {total}")
    total += int(input("How many dimes?: ")) * 0.1
    print(f"Your Have Given: {total}")
    return total

def check_transaction (choice,total):
    global money
    if total>=int(MENU[choice]["cost"]):
        change=total-int(MENU[choice]["cost"])
        money += int(MENU[choice]["cost"])
        print(f"Here is ${round(change,3)} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

while True:
    choice=input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice =="off":
        print("Turning Off")
        exit()
    if choice =="report":
        report()
    if choice == "espresso" or choice == "latte" or choice == "cappuccino":
        if check_resources(choice):
            total=process_coins(choice)
            if check_transaction(choice,total):
                ingredients=MENU[choice]["ingredients"]
                for i in ingredients:
                    resources[i]-=ingredients[i]
                print(f"Here is your {choice} ☕☕. Enjoy!")
