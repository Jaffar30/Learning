import random
cards = {
    "A♠": [11,1], "2♠": 2, "3♠": 3, "4♠": 4, "5♠": 5, "6♠": 6, "7♠": 7, "8♠": 8, "9♠": 9, "10♠": 10, "J♠": 10, "Q♠": 10, "K♠": 10,
    "A♥": [11,1], "2♥": 2, "3♥": 3, "4♥": 4, "5♥": 5, "6♥": 6, "7♥": 7, "8♥": 8, "9♥": 9, "10♥": 10, "J♥": 10, "Q♥": 10, "K♥": 10,
    "A♦": [11,1], "2♦": 2, "3♦": 3, "4♦": 4, "5♦": 5, "6♦": 6, "7♦": 7, "8♦": 8, "9♦": 9, "10♦": 10, "J♦": 10, "Q♦": 10, "K♦": 10,
    "A♣": [11,1], "2♣": 2, "3♣": 3, "4♣": 4, "5♣": 5, "6♣": 6, "7♣": 7, "8♣": 8, "9♣": 9, "10♣": 10, "J♣": 10, "Q♣": 10, "K♣": 10
}
def deal_card():
    return random.choice(list(cards.keys()))

def calculate_score(hand):
    score = 0
    for card in hand:
        if card.startswith('A'):
            if score + 11 > 21:
                score += 1
            else:
                score += 11
        else:
            score += cards[card]
    return score
def blackjack():
    user_hand = []
    computer_hand = []
    for _ in range(2):
        user_hand.append(deal_card())
        computer_hand.append(deal_card())
    while True:
        user_score = calculate_score(user_hand)
        print(f"Your cards: {user_hand}, current score: {user_score}")
        print(f"Computer's first card: {computer_hand[0]}")
        user_should_deal = input("Type 'hit' to get another card, type 'stand' to pass: ")
        if user_should_deal == 'hit':
            user_hand.append(deal_card())
            computer_hand.append(deal_card())
        user_score = calculate_score(user_hand)
        computer_score = calculate_score(computer_hand)
        if user_score > 21:
            print(f"Your final hand: {user_hand}, final score: {user_score}")
            print(f"Computer's final hand: {computer_hand}, final score: {computer_score}")
            print("You went over. You lose")
            break
        elif computer_score > 21:
            print(f"Your final hand: {user_hand}, final score: {user_score}")
            print(f"Computer's final hand: {computer_hand}, final score: {computer_score}")
            print("Opponent went over. You win")
            break

        if user_should_deal == 'stand':
            result(user_hand,computer_hand)
            break

def result(user_hand,computer_hand):
    user_score = calculate_score(user_hand)
    computer_score = calculate_score(computer_hand)
    print(f"Your final hand: {user_hand}, final score: {user_score}")
    print(f"Computer's final hand: {computer_hand}, final score: {computer_score}")
    if user_score > computer_score and user_score <= 21:
        print("You win ")
    elif computer_score > user_score and computer_score <= 21:
        print("You lose ")
    elif user_score == computer_score:
        print("It's a draw ")
    elif computer_score > 21:
        print("Opponent went over. You win")
    elif user_score > 21:
        print("You went over. You lose")
blackjack()