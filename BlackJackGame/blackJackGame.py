import random

def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare_func(u_score, comp_score):
    """Compare the user scores and computer score and return the score"""
    if u_score == comp_score:
        return "Draw :/"
    elif comp_score == 0:
        return "Lose, opponent has Blackjack :)"
    elif u_score == 0:
        return "Win with a Blackjack :)"
    elif u_score > 21:
        return "You went over. You lose :("
    elif comp_score > 21:
        return "Opponent went over. You win :)"
    elif u_score > comp_score:
        return "You win :)"
    else:
        return "You lose :("

def play_game():
    user_cards = []
    computer_cards = []

    # this will give the developer a heads up on a potential error
    computer_score = -1
    user_score = -1
    is_game_over = False

    # run the loop twice
    # gets a new card by calling deal_card()
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer card: {computer_cards[0]}")
        print

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer final hand: {computer_cards}, final score: {computer_score}")
    print(compare_func(user_score, computer_score))


while input("Do you want to play another game of Blackjack? y/n?") == "y":
    print("\n")
    print("WELCOME TO BLACKJACK GAME")
    play_game()
