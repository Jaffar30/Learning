import pandas

nato_csv = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter : row.code for (index, row) in nato_csv.iterrows()}
print("use '0' to exit")
while True:
    user_input = input("Enter word: ").upper()
    if user_input == '0':
        break
    nato_result = [nato_dict[word] for word in user_input]
    print(nato_result)