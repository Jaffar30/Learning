# *args : Many Positional Arguments

def add1(number1,number2):
    return number1 + number2

print(add1(3,6))
# print(add1(3,6,1)) - this gonna give you error how we can improve it using *args

def add2(*args):
    sum = 0
    print(args[-1])
    print(type(args))
    for number in args:
        print(number)
        sum+=number
    return sum

print(add2(3,6,1,1,1))

# value of the *args 
# will take the arguments you passed to the function : (3,6,1,1,1) all of them and convert them to list ?

# CHATGPT:

# What *args really does
# *args:
# Collects positional arguments
# Packs them into a tuple, not a list
# The name args is just a convention