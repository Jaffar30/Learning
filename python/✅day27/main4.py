# **kwargs : Keyworded arguments

def calculate(**kwargs):
    # we now created unlimited keywords arguments
    print(kwargs)
    # {'add': 3, 'multiply': 5}
    # **kwargs convert arguments to dictionary key,value 
    # .items() so we can convert them to tuples so they can be iteretable
    for key,value in kwargs.items():
        print(key,value)
    # add 3
    # multiply 5

calculate(add=3,multiply=5)