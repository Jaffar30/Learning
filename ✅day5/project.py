# password generator
import random

PASSWORD_CHARS = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
    'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
]

PASSWORD_NUMBERS = ['0','1','2','3','4','5','6','7','8','9']

PASSWORD_SYMBOLS = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
    '-', '_', '=', '+', '[', ']', '{', '}', '\\', '|',
    ';', ':', "'", '"', ',', '.', '/', '<', '>', '?',
    '`', '~'
]

def validate_user_option(msg):
    while True:
        user_input = input(msg)
        if user_input.isdigit():   # all characters are digits
            return int(user_input)
        print("Invalid Input! Please enter a number.")


def added_values(count,list):
    user_password = []
    for i in range(int(count)):
        user_password.append(random.choice(list))
    return user_password

# how many letter in the password
letters_needed = validate_user_option("How Many Letter would you like in your password?\n")
# how many symbols
symbols_needed = validate_user_option("How many symbol do you need?\n")
# how many number
numbers_needed = validate_user_option("How many number do you need?\n")

user_password = []
user_password.extend(added_values(letters_needed,PASSWORD_CHARS))
user_password.extend(added_values(symbols_needed,PASSWORD_SYMBOLS))
user_password.extend(added_values(numbers_needed,PASSWORD_NUMBERS))

user2_password = ""
for i in range(len(user_password)):
    user2_password =user2_password+ user_password.pop(random.randrange(len(user_password)))

# you can also use random.shuffle

print(f"Your Password is : {user2_password}")