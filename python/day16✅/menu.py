# tea_menu = {
#     "karak" : {"cost": 0.100, "need": {"water": 200, "milk": 100, "tea_leaves": 10}},
#     "english_tea" : {"cost": 0.150, "need": {"water": 250, "tea_leaves": 15}},
#     "turkish_tea" : {"cost": 0.300, "need": {"water": 220, "tea_leaves": 12}},
#     "irani_tea" : {"cost": 0.500, "need": {"water": 180, "tea_leaves": 14}},
#     "iraqi_tea" : {"cost": 1, "need": {"water": 210, "tea_leaves": 11}},
# }
class Menu:
    def __init__(self):
        self.tea_menu = {
            "karak" : {"cost": 0.100, "need": {"water": 200, "milk": 100, "tea_leaves": 10}},
            "english_tea" : {"cost": 0.150, "need": {"water": 250, "tea_leaves": 15}},
            "turkish_tea" : {"cost": 0.300, "need": {"water": 220, "tea_leaves": 12}},
            "irani_tea" : {"cost": 0.500, "need": {"water": 180, "tea_leaves": 14}},
            "iraqi_tea" : {"cost": 1, "need": {"water": 210, "tea_leaves": 11}},
        }
    def get_items():
        items = ""
        for item in Menu().tea_menu:
            items += f"{item}/"
        return items[:-1]  # Remove the trailing slash
    def find_tea(self, tea_name):
        if tea_name in self.tea_menu:
            return self.tea_menu[tea_name]
        print("Sorry that tea is not available.")
        return None