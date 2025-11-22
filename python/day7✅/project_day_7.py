import hangman
import random

hangman_logo = hangman.hangman_art
hangman_stages = hangman.hangman_stages
hangman_words= hangman.hangman_words

print(hangman_logo)

chosen_word = random.choice(hangman_words)
word_length = len(chosen_word)

placeholder = ""
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
lives = 6

correct_guesses = []

while not game_over:
    guess = input("Guess a letter: ").lower()
    display = ""
    if guess in display:
        --lives
        print(f"You've already guessed {guess}")

    for letter in chosen_word:
        if letter == guess:
            display += guess
            correct_guesses.append(letter)
        elif letter in correct_guesses:
            display += letter
        else:
            display += "_"
    print(display)
# wrong guess condition
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            game_over = True
            print(f"++++++++++++++++++ {chosen_word} You lose ++++++++++++++++++")
    print(hangman_stages[lives])
    print(f"++++++++++++++++++ You have {lives}/6 lives ++++++++++++++++++")
# game win condition
    if "_" not in display:
        game_over = True
        print("++++++++++++++++++ You win ++++++++++++++++++")

