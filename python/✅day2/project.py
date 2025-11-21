print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?")) /100 * total_bill
people_num = int(input("How many people to split the bill?"))


result = (total_bill + tip)/people_num
print(f"Each person should pay: ${"{:.2f}".format(result)}")
