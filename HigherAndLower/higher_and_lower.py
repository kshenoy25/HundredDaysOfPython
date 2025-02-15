
from game_data import data
import random




def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(user_guess, a_followers, b_followers):
    """Take a user's guess and the follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

score = 0
game_should_continue = True
account_b = random.choice(data)
while game_should_continue:
    # generate a random account from the game data
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print("VS")
    print(f"Compare B: {format_data(account_b)}.")

    # ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower() # eliminating case sensitivity

    # check if the user is correct
    ## get the follower count of each account
    ## user the if statement to check if user is correct
    a_follower_account = account_a["follower_count"]
    b_follower_account = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_account, b_follower_account)

    # give the user feedback on their guess
    if is_correct:
        score += 1
        print(f"You are correct! Current score {score}.")
    else:
        print(f"Sorry, you are wrong! Final score is {score}")
        game_should_continue = False



