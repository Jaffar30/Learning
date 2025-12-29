# with open("Learning/python/day25/weather_data.csv") as weather_file:
#     weather_data = weather_file.readlines()

import csv
data = False
tempretures = []
with open("Learning/python/day25/weather_data.csv") as weather_file:
    data = csv.reader(weather_file) # create a csv_reader object <_csv.reader object at 0x000002CCBD58E4A0>
    for index,row in enumerate(data):
        if index == 0:
            continue
        tempretures.append(int(row[1]))
        
        # tempretures.append(int(row[1]))

print(tempretures)