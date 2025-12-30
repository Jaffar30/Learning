# list and dictionary comprehensions

# how to create a list using comprehension
# its a case where you create a new list from an old list
# before we used for loops to create new lists

normal_numbers = []
for number in range(0, 11):
    normal_numbers.append(number)
print(normal_numbers)

comprehension_numbers = [number for number in range(0, 11)]
print(comprehension_numbers)

# Python Sequences : because they have specific order unlike dictionaries:
# list,range,string,tuple
# we can use comprehension with all the above sequences

# conditional list comprehension
even_numbers = [number for number in range(0, 11) if number % 2 == 0]
print(even_numbers)