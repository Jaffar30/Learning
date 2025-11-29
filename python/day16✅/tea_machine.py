# resources = {
#     "water": 1000,
#     "milk": 500,
#     "tea_leaves": 100,
#     "money": 0,
# }


# def is_can_make(need):
#     for item in need:
#         if need[item] > resources[item]:
#             print(f"Sorry there is not enough {item}.")
#             return False
#     return True


# def make_tea(need, cost):
#     for item in need:
#         resources[item] -= need[item]
#     resources["money"] += cost
#     print("Here is your tea. Enjoy!")

# def print_resource():
#     print("The tea machine has:")
#     print(f"{resources['water']}ml of water")
#     print(f"{resources['milk']}ml of milk")
#     print(f"{resources['tea_leaves']}g of tea leaves")
#     print(f"BD{resources['money']} of money")
class TeaMachine:
    resources = {
        "water": 1000,
        "milk": 500,
        "tea_leaves": 100,
        "money": 0,
    }

    @classmethod
    def is_can_make(cls, need):
        for item in need:
            if need[item] > cls.resources[item]:
                print(f"Sorry there is not enough {item}.")
                return False
        return True

    @classmethod
    def make_tea(cls, need, cost):
        for item in need:
            cls.resources[item] -= need[item]
        cls.resources["money"] += cost
        print("Here is your tea")

    @classmethod
    def print_resource(cls):
        print("The tea machine has:")
        print(f"{cls.resources['water']}ml of water")
        print(f"{cls.resources['milk']}ml of milk")
        print(f"{cls.resources['tea_leaves']}g of tea leaves")
        print(f"BD{cls.resources['money']} of money")