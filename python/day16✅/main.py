from menu import Menu
from tea_machine import TeaMachine
from payment import payment
# In this day project I take project from a day15 and class it 
# I used ai support in putting base classes
while True:
    choice = input(f"What would you like? {Menu.get_items()}: ").lower()
    if choice == "off":
        break
    elif choice == "report":
        TeaMachine.print_resource()
    elif choice in Menu().tea_menu:
        tea = Menu().find_tea(choice)
        if TeaMachine.is_can_make(tea["need"]):
            payment = payment().calculate()
            if payment >= tea["cost"]:
                change = payment - tea["cost"]
                if change >= 0:
                    print(f"Here is BD{change} in change.")
                    TeaMachine.make_tea(tea["need"], tea["cost"])
            else:
                print("Sorry that's not enough money. Money refunded.")
    else:
        print("Invalid choice. Please try again.")
        continue