with open("/python2025/python/day24/day24_project/Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("/python2025/python/day24/day24_project/Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace("[name]", stripped_name)
        with open(f"/python2025/python/day24/day24_project/Output/ReadyToSend/letter_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
        
        
