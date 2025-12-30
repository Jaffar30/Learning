import pandas


# how to use loops in pandas dataframe

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

for (key,value) in student_dict.items():
    print(value)

# you can consider working with dataframes as working with dictionaries

student_data = pandas.DataFrame(student_dict)

print(student_data)

# Loop through a dataframe using same method as dictionaries

for (key, value) in student_data.items():
    print(value)

# keys : student, score
# values : 
# 0    Angela
# 1      James
# 2       Lily
# Name: student, dtype: object


# it has a function called iterrows() : it allows you to loop through each row of a dataframe

for (index, row) in student_data.iterrows():
    print(index)
    print(row)
    print(row.student)
    print(row.score)