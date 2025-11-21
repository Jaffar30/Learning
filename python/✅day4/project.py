import random

options = [

"""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

,

"""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

,

"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

]


user_option = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
while user_option not in ['0','1','2']:
    print("Invalid Input")
    user_option = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")

user_option = int(user_option)
print(options[user_option])
print("Computer chose:")
computer_option = random.randint(0,2)
print(options[computer_option])

if user_option == computer_option:
    print("You Draw")
elif (user_option - computer_option) % 3 == 1:
    print("You Win")
else:
    print("You Lost")
