MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 10,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 15,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 15,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0
make_drink = True
paid = False
drinks = MENU.keys()

res = {
    "water": resources["water"],
    "milk": resources["milk"],
    "coffee": resources["coffee"],
}


def change(cost):
    one = int(input("how many R1: "))
    two = int(input("how many R2: "))
    five = int(input("how many R5: "))
    ten = int(input("how many R10: "))
    inserted_money = one * 1 + two * 2 + five * 5 + ten * 10
    if cost > inserted_money:
        print(f"You are short R{cost - inserted_money}, money refunded")
        return False
    else:
        print(f"Thank you, here is your change of R{inserted_money - cost}")
        return True


off = False
while not off:
    for drink in drinks:
        price = MENU[drink]["cost"]
        print(f"{drink} \t\tPrice: {price}")

    # TODO: user picks a beverage
    choice = input("please select a beverage").lower()
    if choice == "off":
        off = True
    elif choice == "report":
        for resource, value in resources.items():
            print(f"{resource}: {value}")
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        drink_resources = MENU[choice]["ingredients"].items()

        for ingredient, value in drink_resources:
            difference = resources[ingredient] - value
            if difference < 0:
                print(f"Sorry, machine does not have enough {ingredient}")
                make_drink = False
            else:
                res[ingredient] = difference

        if make_drink:
            paid = change(MENU[choice]["cost"])
        if paid:
            profit += MENU[choice]["cost"]

        if paid and make_drink:
            resources["water"] = res["water"]
            resources["milk"] = res["milk"]
            resources["coffee"] = res["coffee"]
            resources["money"] = profit
            print(f"Here is your {choice}, enjoy!")

    else:
        print("not a valid choice")
