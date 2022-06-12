from menu import MENU

coin_values = [
    {"quarters": 0.25},
    {"dimes": 0.1},
    {"nickles": 0.05},
    {"pennies": 0.01}
]


def show_report(resources, money):
    print(f"\n{'Water:'.ljust(7)} {resources['water']}ml")
    print(f"{'Milk:'.ljust(7)} {resources['milk']}ml")
    print(f"{'Coffee:'.ljust(7)} {resources['coffee']}g")
    print(f"{'Money:'.ljust(7)} ${money}\n")


def is_resources_enough(resources, drink):
    flag = True
    for ingredient in MENU[drink]["ingredients"]:
        if resources[ingredient] < MENU[drink]["ingredients"][ingredient]:
            print(f"Sorry there is not enough {ingredient}")
            flag = False
    return flag


def insert_money():
    amount = 0
    for coin in coin_values:
        for name, value in coin.items():
            amount += int(input(f"How many {name}?: ")) * value
    return amount


def is_money_enough(money, drink):
    if money >= MENU[drink]["cost"]:
        return True
    else:
        return False


def need_change(money, drink):
    if money > MENU[drink]["cost"]:
        refund_amount = round(money - MENU[drink]["cost"], 2)
        print(f"Here is ${refund_amount} in change.")
        return refund_amount
    else:
        return


def make_drink(resources, drink):
    for ingredient in resources:
        resources[ingredient] -= MENU[drink]["ingredients"][ingredient]
    return resources


def refund_money(cashbox, refund_amount):
    cashbox -= refund_amount
    return cashbox


current_resources = {
    "water": 5000,
    "milk": 2000,
    "coffee": 1000,
}
total_money = 0


def main(resources, cashbox):
    turn_off_machine = True
    while turn_off_machine:
        command = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if command == "report":
            show_report(resources, cashbox)
        elif command in MENU:
            if is_resources_enough(resources, command):
                print("Please insert money.")
                inserted_money = insert_money()
                cashbox += inserted_money
                if is_money_enough(inserted_money, command):
                    cashbox -= need_change(inserted_money, command)
                    resources = make_drink(resources, command)
                    print(f"Here is your {command}. Enjoy!☕☕☕")
                else:
                    print("Sorry that's not enough money. Money refunded.")
                    cashbox = refund_money(cashbox, inserted_money)
                    continue
            else:
                continue
        if command == "off":
            return resources, cashbox


if __name__ == "__main__":
    current_resources, total_money = main(current_resources, total_money)
