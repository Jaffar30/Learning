import pandas

data = pandas.read_csv("Learning/python/day25/weather_data.csv")
print(type(data)) # <class 'pandas.core.frame.DataFrame'>
print(type(data["temp"])) # <class 'pandas.core.series.Series'>
html_data = data.to_html() # convert data to html format
print(html_data)
data_dict = data.to_dict() # convert data to dictionary format
print(data_dict)
temp_list = data["temp"].to_list() # convert a column to list
print(temp_list)
# you can convert data to many formats like json, csv, html, excel, etc.

# in the documents there is a 2 types Series (1-dimensional) and DataFrame (2-dimensional)
#                                             only one column                excel sheet
#                                           (like a list)               (like a table)