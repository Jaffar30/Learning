
LETTERS = [
    # Lowercase letters
    'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
    # Uppercase letters
    'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
    # Numbers
    '0','1','2','3','4','5','6','7','8','9',
    # Special characters
    '!','@','#','$','%','^','&','*','(',')','-','_','=','+','[',']','{','}',';',':','"',',','.','<','>','/','?','|','\\'
]



def encode(user_msg):
    new_msg = []
    for letter in user_msg:
        new_msg.append(LETTERS[LETTERS.index(letter)+user_shift%len(LETTERS)])
    return "".join(new_msg)

def decode(user_msg):
    new_msg = []
    for letter in user_msg:
        new_msg.append(LETTERS[LETTERS.index(letter)-user_shift%len(LETTERS)])
    return "".join(new_msg)

while(True):
    user_input = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    user_msg = input("Type your message:\n")
    user_shift = int(input("Type the shift number:\n"))

    if user_input == 'encode':
        print(encode(user_msg))
    elif user_input == 'decode':
        print(decode(user_msg))



# VERSION WITH VALIDATION 

# LETTERS = [
#     # Lowercase letters
#     'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
#     # Uppercase letters
#     'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
#     # Numbers
#     '0','1','2','3','4','5','6','7','8','9',
#     # Special characters
#     '!','@','#','$','%','^','&','*','(',')','-','_','=','+','[',']','{','}',';',':','"',',','.','<','>','/','?','|','\\'
# ]

# def encode(user_msg, user_shift):
#     new_msg = []
#     for letter in user_msg:
#         if letter in LETTERS:
#             new_index = (LETTERS.index(letter) + user_shift) % len(LETTERS)
#             new_msg.append(LETTERS[new_index])
#         else:
#             new_msg.append(letter)  # Keep unknown characters as-is
#     return "".join(new_msg)

# def decode(user_msg, user_shift):
#     new_msg = []
#     for letter in user_msg:
#         if letter in LETTERS:
#             new_index = (LETTERS.index(letter) - user_shift) % len(LETTERS)
#             new_msg.append(LETTERS[new_index])
#         else:
#             new_msg.append(letter)  # Keep unknown characters as-is
#     return "".join(new_msg)

# while True:
#     user_input = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
#     user_msg = input("Type your message:\n")

#     # Validate shift input
#     while True:
#         try:
#             user_shift = int(input("Type the shift number:\n"))
#             break
#         except ValueError:
#             print("Please enter a valid number for shift.")

#     if user_input == 'encode':
#         print("Encrypted message:", encode(user_msg, user_shift))
#     elif user_input == 'decode':
#         print("Decrypted message:", decode(user_msg, user_shift))
#     else:
#         print("Invalid option. Type 'encode' or 'decode'.")
