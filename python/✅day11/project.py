import random
from pprint import pprint

cards = {
    "A♠": [11,1], "2♠": 2, "3♠": 3, "4♠": 4, "5♠": 5, "6♠": 6, "7♠": 7, "8♠": 8, "9♠": 9, "10♠": 10, "J♠": 10, "Q♠": 10, "K♠": 10,
    "A♥": [11,1], "2♥": 2, "3♥": 3, "4♥": 4, "5♥": 5, "6♥": 6, "7♥": 7, "8♥": 8, "9♥": 9, "10♥": 10, "J♥": 10, "Q♥": 10, "K♥": 10,
    "A♦": [11,1], "2♦": 2, "3♦": 3, "4♦": 4, "5♦": 5, "6♦": 6, "7♦": 7, "8♦": 8, "9♦": 9, "10♦": 10, "J♦": 10, "Q♦": 10, "K♦": 10,
    "A♣": [11,1], "2♣": 2, "3♣": 3, "4♣": 4, "5♣": 5, "6♣": 6, "7♣": 7, "8♣": 8, "9♣": 9, "10♣": 10, "J♣": 10, "Q♣": 10, "K♣": 10
}

print("Welcome to BlackJack")
dealler_cards = {}
player_cards = {}

def sum_card_value(cards):
    sum = 0
    aces = 0
    for card in cards:
        if card in ['A♠','A♥','A♦','A♣']:
            aces = aces + 1
            continue
        sum+= cards[card]

    for i in range(aces):
        sum += 11 if sum + 11 <= 21 else 1
    
    return sum


def draw_one_card():
    card = {}
    card1 = random.choice(list(cards.keys()))
    card[card1] = cards.pop(card1)
    return card

def draw_2cards():
    return {**draw_one_card(), **draw_one_card()} 

def print_cards(cards):
    cards_list = list(cards.keys())  
    print(" - ".join(cards_list))
    cards_sum = sum_card_value(cards)
    print(f"Sum: {cards_sum}")
    return cards_sum
    

def get_valid_hit_stand(question):
    user_input = input(str(question)).lower()

    while(user_input.strip()=='' or user_input not in ['hit','stand']):
        user_input = input("Invalid Input Try Again :").lower()
    
    return user_input == 'hit'


    

player_cards.update(draw_2cards())
dealler_cards.update(draw_2cards())

def dealler_draws():
    print("Dealler Turn to Draw")
    dealer_sum = print_cards(dealler_cards)
    while(dealer_sum < 17):
        dealler_cards.update(draw_one_card())
        dealer_sum = print_cards(dealler_cards)
    return dealer_sum

print("Dealer Cards:")
print(f"{random.choice(list(dealler_cards.keys()))} - #")
         
print("Your Cards:")
player_sum = print_cards(player_cards)

user_input = get_valid_hit_stand(question="Type hit to draw or stand to stop: ")

while(user_input):
    player_cards.update(draw_one_card())
    player_sum = print_cards(player_cards)
    if player_sum > 21:
        break
    user_input = get_valid_hit_stand(question="Type hit to draw or stand to stop: ")

dealer_sum = dealler_draws()

if player_sum == 21:
    print("You win")
elif player_sum > 21:
    print("You lost")
else:
    if player_sum > dealer_sum:
        print("You win")
    else:
        print("Dealer Win")