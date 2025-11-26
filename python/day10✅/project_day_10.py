# def addition(a, b):
#     return a + b
# def subtraction(a, b):
#     return a - b
# def multiplication(a, b):
#     return a * b
# def division(a, b):
#     if b == 0:
#         return "Error: Division by zero"
#     return a / b

# number1 = int(input("Enter first the number: "))
# while True:
#     input_operator = input("Enter the operator (+, -, *, /) or 'q' to quit: ")
#     if input_operator == 'q':
#         break
#     number2 = int(input("Enter the second number: "))
#     if input_operator == '+':
#         result = addition(number1, number2)
#     elif input_operator == '-':
#         result = subtraction(number1, number2)
#     elif input_operator == '*':
#         result = multiplication(number1, number2)
#     elif input_operator == '/':
#         result = division(number1, number2)
#     else:
#         print("Invalid operator. Please try again.")
#         continue
#     print(f"{number1} {input_operator} {number2} = {result}")
#     number1 = result

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b
operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}
def calculator():
    number1 = float(input("Enter the first number: "))
    while True:
        operator = input("Enter an operator (+, -, *, /) or 'q' to quit: ")
        if operator == 'q':
            print("Goodbye!")
            break
        if operator not in operations:
            print("Invalid operator. Please try again.")
            continue
        number2 = float(input("Enter the second number: "))
        result = operations[operator](number1, number2)
        print(f"{number1} {operator} {number2} = {result}")
        number1 = result
calculator()