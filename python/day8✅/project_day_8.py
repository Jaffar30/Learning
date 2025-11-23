alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caser(text, shift, type):
    reuslt = ""
    if type == "decode":
        shift *= -1
    for character in text:
        if character not in alphabet:
            reuslt += character
        else:
            reuslt += alphabet[(alphabet.index(character) + shift) % len(alphabet)]
    print(f"The {type}d text is {reuslt}")

do_again = True
while do_again:
    type = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Enter the original text: ")
    shift = int(input("Enter the shift number: "))
    caser(text, shift, type)
    check = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if check == "no":
        do_again = False