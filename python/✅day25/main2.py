import pandas

data = pandas.read_csv("Learning/python/day25/weather_data.csv")
print(data["temp"])
print(data)



# formmatted output:
#          day  temp condition
# 0     Monday    12     Sunny
# 1    Tuesday    14      Rain
# 2  Wednesday    15      Rain
# 3   Thursday    14    Cloudy
# 4     Friday    21     Sunny
# 5   Saturday    22     Sunny
# 6     Sunday    24     Sunny


# print(data["temp"]) this will print the temp column only

# Output:
# 0    12
# 1    14
# 2    15
# 3    14
# 4    21
# 5    22
# 6    24