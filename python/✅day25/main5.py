import pandas

# Create a sample DataFrame from scratch
data_dict = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [24, 30, 22, 35],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}

data = pandas.DataFrame(data_dict)
print(data)

data.to_csv("new_data.csv", index=False)  # Save DataFrame to CSV without the index column
