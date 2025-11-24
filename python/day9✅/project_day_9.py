is_continue = True
pid_list = {}
def winner(pid_record):
    highest_pid = 0
    winner_name = ""
    for name in pid_record:
        if pid_record[name] > highest_pid:
            highest_pid = pid_record[name]
            winner_name = name
    print(f"The winner is {winner_name} with a pid of BHD{highest_pid}")
    

while is_continue:
    name = input("Enter your name: ")
    pid_amount = int(input("How much will pid: BHD"))
    pid_list[name] = pid_amount
    should_continue = input("Do you want to add another entry? Type 'yes' or 'no': ").lower()
    if should_continue == 'no':
        winner(pid_list)
        is_continue = False
        