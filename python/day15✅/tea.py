tea_menu = {
    "karak" : {"cost": 0.100, "need": {"water": 200, "milk": 100, "tea_leaves": 10}},
    "english_tea" : {"cost": 0.150, "need": {"water": 250, "tea_leaves": 15}},
    "turkish_tea" : {"cost": 0.300, "need": {"water": 220, "tea_leaves": 12}},
    "irani_tea" : {"cost": 0.500, "need": {"water": 180, "tea_leaves": 14}},
    "iraqi_tea" : {"cost": 1, "need": {"water": 210, "tea_leaves": 11}},
}


resources = {
    "water": 1000,
    "milk": 500,
    "tea_leaves": 100,
    "money": 0,
}


def is_can_make(need):
    for item in need:
        if need[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def make_tea(need, cost):
    for item in need:
        resources[item] -= need[item]
    resources["money"] += cost
    print("Here is your tea. Enjoy!")

def print_resource():
    print("The tea machine has:")
    print(f"{resources['water']}ml of water")
    print(f"{resources['milk']}ml of milk")
    print(f"{resources['tea_leaves']}g of tea leaves")
    print(f"BD{resources['money']} of money")


def money_calc():
    print("Please insert coins.")
    total = 0
    # total += int(input("How many dinar?: ")) * 1.000
    # total += int(input("How many half dinar?: ")) * 0.500
    # total += int(input("How many 100 fils?: ")) * 0.100
    # total += int(input("How many 50 fils?: ")) * 0.050
    try:
        total += int(input("How many dinar?: ")) * 1.000
        total += int(input("How many half dinar?: ")) * 0.500
        total += int(input("How many 100 fils?: ")) * 0.100
        total += int(input("How many 50 fils?: ")) * 0.050
    except ValueError:
        print("Invalid input. Please enter numeric values for coins.")
        return money_calc()
    
    return total


def tea_machine():
    while True:
        choice = input("What would you like? (karak/english_tea/turkish_tea/irani_tea/iraqi_tea): ").lower()
        if choice == "off":
            break
        elif choice == "report":
            print_resource()
        elif choice in tea_menu:
            tea = tea_menu[choice]
            if is_can_make(tea["need"]):
                payment = money_calc()
                if payment >= tea["cost"]:
                    change = payment - tea["cost"]
                    if change >= 0:
                        print(f"Here is BD{change} in change.")
                    make_tea(tea["need"], tea["cost"])
                else:
                    print("Sorry that's not enough money. Money refunded.")
        else:
            print("Invalid choice. Please try again.")
            continue
tea_machine()