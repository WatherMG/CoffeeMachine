FILL_SUPPLIES = "fill"
TAKE_MONEY = "take"
BUY_COFFEE = "buy"
REMAINING = "remaining"
machine_supplies = {"water": 400, "milk": 540, "beans": 120, "cups": 9, "money": 550}
running = True


def interface():
    print("\nThe coffee machine has:")
    print(f"{machine_supplies.get('water')} of water")
    print(f"{machine_supplies.get('milk')} of milk")
    print(f"{machine_supplies.get('beans')} of coffee beans")
    print(f"{machine_supplies.get('cups')} of disposable cups")
    print(f"${machine_supplies.get('money')} of money\n")


def fill_supplies():
    water = int(input("\nWrite how many ml of water you want to add:\n"))
    milk = int(input("Write how many ml of milk you want to add:\n"))
    beans = int(input("Write how many grams of coffee beans you want to add:\n"))
    cups = int(input("Write how many disposable coffee cups you want to add:\n"))
    supplies = {"water": water, "milk": milk, "beans": beans, "cups": cups}
    for key in machine_supplies.keys():
        if key in supplies:
            machine_supplies[key] += + supplies[key]
    print()


def take_money():
    print(f"\nI gave you ${machine_supplies.get('money')}\n")
    machine_supplies['money'] = 0


def make_coffee(choice):
    enough_resources = True
    for key in machine_supplies.keys():
        if key in choice.keys() and key != "money":
            supply = machine_supplies[key] - choice[key]
            if supply > 0:
                machine_supplies[key] -= choice[key]
            else:
                enough_resources = False
                return enough_resources, key
    machine_supplies["money"] += choice["money"]
    return enough_resources, ""


def buy_coffee():
    user_choice = input("\nWhat do you want to buy? 1 - espresso, 2 - latte, "
                        "3 - cappuccino, back - to main menu:\n")
    if user_choice == "back":
        print()
        return user_choice
    espresso = {"water": 250, "beans": 16, "cups": 1, "money": 4}
    latte = {"water": 350, "milk": 75, "beans": 20, "cups": 1, "money": 7}
    cappuccino = {"water": 200, "milk": 100, "beans": 12, "cups": 1, "money": 6}
    choices = [espresso, latte, cappuccino]
    enough, resource = make_coffee(choices[int(user_choice) - 1])
    print(f"{'I have enough resources, making you a coffee!' if enough else 'Sorry, not enough ' + resource + '!'}")
    print()


def menu(user_action):
    global running
    if user_action == FILL_SUPPLIES:
        fill_supplies()
    elif user_action == TAKE_MONEY:
        take_money()
    elif user_action == BUY_COFFEE:
        buy_coffee()
    elif user_action == "exit":
        running = False
    elif user_action == REMAINING:
        interface()


def run():
    while running:
        action = input("Write action (buy, fill, take, remaining, exit):\n")
        menu(action)


if __name__ == '__main__':
    run()
