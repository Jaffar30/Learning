print("Welcome to the secret auction program.")
bids = {}

def get_valid_string_input(question):
    user_input = input(str(question))

    while(user_input.strip()=='' or bids.get(user_input)):
        user_input = input("Invalid Input Try Again :")
    return user_input

def get_valid_number_input(question):
    user_input = input(str(question))

    while(user_input.strip()=='' or not user_input.isdigit() or int(user_input)<=0):
        user_input = input("Invalid Input Try Again :")
    return int(user_input)

def get_valid_yes_no(question):
    user_input = input(str(question)).lower()

    while(user_input.strip()=='' or user_input not in ['yes','no']):
        user_input = input("Invalid Input Try Again :").lower()
    
    return user_input == 'yes'


while(True):
    name = get_valid_string_input(question="What is your name? : ")
    bid = get_valid_number_input(question="What's your bid? : ")
    bids[name]=bid
    is_still_bids = get_valid_yes_no(question="Are there any other bidders? Type 'yes' or 'no'. \n")    
    print("\n"*100)
    if not is_still_bids:
        break


winner = max(bids,key=bids.get)
print(f"The winner is {winner} with :${bids[winner]}")

    
    