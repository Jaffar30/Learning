import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_data = pandas.DataFrame(student_dict)


for (index, row) in student_data.iterrows():
    print(index)
    print(row)
    print(row.student)
    print(row.score)