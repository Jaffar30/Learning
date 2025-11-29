import random 
data_compare = [
    {"name": "Instagram", "follower_count": 346, "description": "Social media platform", "country": "United States"},
    {"name": "Cristiano Ronaldo", "follower_count": 215, "description": "Footballer", "country": "Portugal"},
    {"name": "Ariana Grande", "follower_count": 183, "description": "Musician and actress", "country": "United States"},
    {"name": "Dwayne Johnson", "follower_count": 181, "description": "Actor and professional wrestler", "country": "United States"},
    {"name": "Selena Gomez", "follower_count": 174, "description": "Musician and actress", "country": "United States"},
    {"name": "Kylie Jenner", "follower_count": 172, "description": "Reality TV personality and businesswoman", "country": "United States"},
    {"name": "Kim Kardashian", "follower_count": 167, "description": "Reality TV personality and businesswoman", "country": "United States"},
    {"name": "Lionel Messi", "follower_count": 149, "description": "Footballer", "country": "Argentina"},
    {"name": "Beyoncé", "follower_count": 145, "description": "Musician", "country": "United States"},
    {"name": "Neymar", "follower_count": 138, "description": "Footballer", "country": "Brazil"},
]

def get_random_account():
    return random.choice(data_compare)
def get_account_info(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

def check(guess, a_followers, b_followers):
    return (guess == 'a' and a_followers > b_followers) or (guess == 'b' and b_followers > a_followers)

def higher_lower_game():
    secore = 0
    account_a = get_random_account()
    account_b = get_random_account()
    if account_a == account_b:
        account_b = get_random_account()
    while True:
        print(f"Compare A: {get_account_info(account_a)}")
        print("VS")
        print(f"Compare B: {get_account_info(account_b)}")
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_followers = account_a["follower_count"]
        b_followers = account_b["follower_count"]
        is_correct = check(guess, a_followers, b_followers)
        if is_correct:
            secore += 1
            print(f"You're right! Current score: {secore}.")
            if guess == 'a':
                account_b = get_random_account()
            else:
                account_a = account_b
                account_b = get_random_account()
                if account_a == account_b:
                    account_b = get_random_account()
        else:
            print(f"Sorry, that's wrong. Final score: {secore}.")
            if input("Do you want to play again? Type 'y' or 'n': ").lower() == 'y':
                higher_lower_game()
            break
higher_lower_game()