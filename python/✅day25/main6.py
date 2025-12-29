import pandas

data = pandas.read_csv('data.csv')
colors = data["Primary Fur Color"].dropna().unique().tolist()

csv_data = {}
for color in colors:
    print(color)
    count = len(data[data["Primary Fur Color"] == color])
    csv_data[color] = count

print(csv_data)

new_data = pandas.DataFrame(csv_data.items(), columns=['Color', 'Count'])
new_data.to_csv('squirrel_count.csv',index=False)



# .items() method in Python is used to return a view object that displays a list of a dictionary's key-value tuple pairs. It allows you to iterate over the keys and values in a dictionary simultaneously.
# example_dict = {'a': 1, 'b': 2, 'c': 3}
# for key, value in example_dict.items():
#     print(f"Key: {key}, Value: {value}")
# results : [('a', 1), ('b', 2), ('c', 3)]