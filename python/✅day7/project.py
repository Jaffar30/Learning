# hangman game

# case uses
# -----------------------------------------------------------------------------
# text = "Python is fun"
# result = text.split()
# print(result)
# Output: ['Python', 'is', 'fun']
# -----------------------------------------------------------------------------
# data = "apple, banana, cherry"
# result = data.split(", ")
# print(result)
# Output: ['apple', 'banana', 'cherry']
# -----------------------------------------------------------------------------
# text = "one,two,three,four"
# result = text.split(",", 2)
# print(result)
# Output: ['one', 'two', 'three,four']
# -----------------------------------------------------------------------------

# you can concatinate a string like this :
# test = "test" "2test"

import random

HANGMANPICS = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''
  +---+
  |   |
      |
      |
      |
      |
=========''']


OPTIONS = [
    'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
]

print("WELCOME TO HANGMAN GAME")

WORDS_LIST = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()


GAME_WORD = random.choice(WORDS_LIST).upper()
player_life = len(HANGMANPICS)-1
player_guesses = []
player_word = ['_' for i in GAME_WORD]

def get_valid_user_input():
    player_input = input("Guess a letter: ").upper()
    while len(player_input) != 1 or player_input not in OPTIONS or player_input in player_guesses:
        player_input = input("Invalid Input Guess Again: ").upper()
    return player_input
        
def add_correct_letters_to_the_player_word(player_input):
    for i,letter in enumerate(GAME_WORD):
        if letter == player_input:
            player_word[i] = letter
        



print(GAME_WORD)
print(player_word)

while player_life > 0 and "_" in player_word:
    print(f"********** {player_life} / {len(HANGMANPICS)-1} **********")
    print(f"Your Letters Guesses: {" ".join(player_guesses)}")
    print(f"Word to guess: {"".join(player_word)}")
    player_input = get_valid_user_input()
    player_guesses.append(player_input)

    if player_input in GAME_WORD:
        add_correct_letters_to_the_player_word(player_input)
        msg = f"You guessed {player_input}, it's in the word."
        if not "_" in player_word:
            msg = f"You Won 👏 the word is {GAME_WORD}"
    else:
        player_life = player_life - 1
        msg = f"You guessed {player_input}, that's not in the word. You lose a life."
        if player_life == 0:
            msg = f"You Lost 💀 the word is {GAME_WORD}"

    print(msg)
    print(HANGMANPICS[player_life])
