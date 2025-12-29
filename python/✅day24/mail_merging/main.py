names = []
with open(r"Learning/python/day24/mail_merging/input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
   
for name in names:
    print(name.strip()) # Remove any extra whitespace/newline characters
    with open(r"Learning/python/day24/mail_merging/input/Letters/starting_letter.txt") as letter_file:
        letter_contents = letter_file.read()
        new_letter = letter_contents.replace("[name]",name.strip())
    with open(f"Learning/python/day24/mail_merging/output/ready_to_send/letter_for_{name.strip()}.txt", mode="w") as completed_letter:
        completed_letter.write(new_letter)