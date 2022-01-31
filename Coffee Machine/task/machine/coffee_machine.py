def initiation():
    water = int(input("Write how many ml of water the coffee machine has:\n"))
    milk = int(input("Write how many ml of milk the coffee machine has:\n"))
    beans = int(input("Write how many grams of coffee beans the coffee machine has:\n"))
    return {"water": water, "milk": milk, "beans": beans}


def calc_coffee():
    cup = {"water": 200, "milk": 50, "beans": 15}
    amount_water = store["water"] // cup["water"]
    amount_milk = store["milk"] // cup["milk"]
    amount_beans = store["beans"] // cup["beans"]
    return min(amount_water, amount_milk, amount_beans)


def interface():
    max_coffee_cups = calc_coffee()
    if cups == max_coffee_cups:
        print("Yes, I can make that amount of coffee")
    elif cups > max_coffee_cups:
        print(f"No, I can make only {max_coffee_cups} cups of coffee")
    elif max_coffee_cups - cups >= 1:
        print(f"Yes, I can make that amount of coffee (and even {max_coffee_cups - cups} more than that)")


if __name__ == '__main__':
    store = initiation()
    cups = int(input("Write how many cups of coffee you will need:\n"))
    interface()
