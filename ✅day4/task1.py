# randomization
# python use this random number generator function : Mersenne Twister

# import library
# python module 
import random
import my_module

# random from [1,2,3] 1-3 included
print(random.randint(1,3))
print(my_module.my_number)

# generate float number
# generate number from 0 included to less than 1 (1 not included)
r = random.random()
print(r)

# from 0 - less than 10
print(r*10)

# same as the upper function where we multiple random with int number
rrr = random.uniform(0,10)
print(rrr)