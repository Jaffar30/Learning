import pandas
# import statistics

data = pandas.read_csv("Learning/python/day25/weather_data.csv")


# avg = statistics.mean(data["temp"].to_list())
# avg = sum(data["temp"]) / len(data["temp"]) 

avg = data["temp"].mean()
max_temp = data["temp"].max()


print(f"Average temperature: {avg} - Max temperature: {max_temp}")

# get data in columns
print(data["condition"])
print(data.condition)

# data in a row
print(data[data.day == "Monday"])


print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)
print(monday.temp * 9/5 + 32) # Celsius to Fahrenheit