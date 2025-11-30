# classes use pascal case : example MyFirstClass
# work this way but not recommended
# class User:
#     pass
# user = User()
# user.name = "John"
# print(user)        
# print(user.name)  

# best use
class User:
    ID_COUNT = 0
    # constructor
    def __init__(self, name, age):
        User.ID_COUNT += 1   # increment class variable
        self.id = User.ID_COUNT
        self.name = name
        self.age = age


user1 = User("John", 30)
print(user1.id)  # 1

user2 = User("Jane", 25)
print(user2.id)  # 2
