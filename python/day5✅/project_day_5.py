import random

letter =  [ 'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' , 'z' ]
number = [ '0' , '1' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' ]
symbol = [ '!' , '#' , '$' , '%' , '&' , '(' , ')' , '*' , '+' ]

print("Welcome to the PyPassword Generator!")
number_letters= int(input("How many letters would you like in your password?\n"))
number_symbols = int(input(f"How many symbols would you like?\n"))
number_numbers = int(input(f"How many numbers would you like?\n"))

password_list = []
for char in range(0, number_letters):
    password_list.append(random.choice(letter))
for char in range(0, number_symbols):
    password_list.append(random.choice(symbol))
for char in range(0, number_numbers):
    password_list.append(random.choice(number))
random.shuffle(password_list)
password = ""
for char in password_list:
    password += char
print(f"Your password is: {password}")
