import random
print("Welcom to guess the number game!")
def guess_the_number():
    print("I'm thinking of a number between 1 and 100")
    deff = input("Choose a difficulty Type 'easy' or 'hard': ")
    if deff == 'easy':
        attempts = 10
    else:
        attempts = 5
    number = random.randint(1, 100)
    guess = 0
    while guess != number and attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))
        if guess > 100 or guess < 1:
            print("Please guess a number within the range 1-100")
            continue
        if guess < number:
            print("Too low")
        elif guess > number:
            print("Too high")
        else:
            print(f"You got it! The answer was {number}")
            return
        attempts -= 1
        if attempts == 0:
            print(f"You've run out of guesses The number was {number}")
        else:
            print("Guess again")
guess_the_number()