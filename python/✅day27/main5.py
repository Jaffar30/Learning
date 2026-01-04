class Car:

    def __init__(self,**kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.doors = kwargs.get("doors") # default value will be None


GTR = Car(make="red",model="GTR",tires="4")
print(GTR.make)
print(GTR.model)
print(GTR.doors)



def test(n,*args,**kwargs):
    print("------------------------")
    print(n)
    # print("----------------------")
    # print(n2)
    print("-------------------------")
    print(args)
    print("---------------------")
    print(kwargs)

# I added a n2 argument after *args this will not work if you want you should add them before *args else its never gonna get a value unless you add a default value but in this case its only
# gonna get a default value so whats the point
test(1,2,3,4,model="test",make="make2")