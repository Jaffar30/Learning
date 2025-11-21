# len(list) : return length of an array : string,bytes,typle,list,range

import sys


print(len("12345"))
print(len([1,2,3,4,5]))
print(len((1,2,3,4,5)))

# how to check data types in python type(data)

print(type("Hello")) #string
print(type(123)) #int
print(type(True)) #bool
print(type(False)) #bool
print(type(1)) #int
print(type(0)) #int
print(type(1.3)) #float
print(type([1,2,3])) #list 
print(type((1,2,3))) #typle

# convert data from one to another called (type conversion) or (type casting)
print("------")
print(type(int("123")))
print(type(str(123)))
print(type(bool(123)))
# you can't convert everything to another
# print(type(list(123)))
print(type(list("123")))
print(type(tuple("123")))
print(type(float(123)))

print("---------")
print(type(None))

sys.exit(0)