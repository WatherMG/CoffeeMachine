FILL_SUPPLIES = "fill"
TAKE_MONEY = "take"
BUY_COFFEE = "buy"
machine_supplies = {"water": 400, "milk": 540, "beans": 120, "cups": 9, "money": 550}


def interface():
    print("The coffee machine has:")
    print(f"{machine_supplies.get('water')} of water")
    print(f"{machine_supplies.get('milk')} of milk")
    print(f"{machine_supplies.get('beans')} of coffee beans")
    print(f"{machine_supplies.get('cups')} of disposable cups")
    print(f"{machine_supplies.get('money')} of money")


def fill_supplies():
    water = int(input("Write how many ml of water you want to add:\n"))
    milk = int(input("Write how many ml of milk you want to add:\n"))
    beans = int(input("Write how many grams of coffee beans you want to add:\n"))
    cups = int(input("Write how many disposable coffee cups you want to add:\n"))
    supplies = {"water": water, "milk": milk, "beans": beans, "cups": cups}
    for key in machine_supplies.keys():
        if supplies.get(key):
            machine_supplies[key] += + supplies[key]
    print()
    interface()


def take_money():
    print(f"I gave you ${machine_supplies.get('money')}")
    machine_supplies['money'] = 0
    print()
    interface()


def make_coffee(coffee):
    for key in machine_supplies.keys():
        if key in coffee.keys() and key != "money":
            machine_supplies[key] -= coffee[key]
    machine_supplies["money"] += coffee["money"]


def buy_coffee():
    coffee_cup = int(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n"))
    espresso = {"water": 250, "beans": 16, "cups": 1, "money": 4}
    latte = {"water": 350, "milk": 75, "beans": 20, "cups": 1, "money": 7}
    cappuccino = {"water": 200, "milk": 100, "beans": 12, "cups": 1, "money": 6}
    choices = [espresso, latte, cappuccino]
    make_coffee(choices[coffee_cup - 1])
    print()
    interface()


def menu(user_action):
    if user_action == FILL_SUPPLIES:
        fill_supplies()
    elif user_action == TAKE_MONEY:
        take_money()
    elif user_action == BUY_COFFEE:
        buy_coffee()


if __name__ == '__main__':
    interface()
    action = input("\nWrite action (buy, fill, take):\n")
    menu(action)
