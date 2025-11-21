print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
# tip is % of bill if tip = 10 then 10/100 = 0.1 
# total bill = bill + (bill * (tip / 100)) if bill 100 and tip is 10 = 100 + 10/100 * 100 = 110
# another way to do it is total bill = bill * (1 + (tip / 100) --> 1 + 0.1) it will return same result
tip_cal = 1 + (tip / 100) 
total_bill = round((bill * tip_cal) / people , 2)
print(f"Each person should pay: ${total_bill}")
