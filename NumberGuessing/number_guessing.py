from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


# function to check users' guess against the actual answer
def check_answer(user_guess, the_answer, turns):
    """Checks answer against the guess and returns number of turns remaining"""
    if user_guess > the_answer:
        print("Too high!")
        return turns - 1
    elif user_guess < the_answer:
        print("Too low!")
        return turns - 1
    else:
        print(f"Correct! The answer was {the_answer}")

# function to set the difficulty
def set_difficulty():
    choose_level_diff = input("Choose a difficulty level: Type 'easy' or 'hard': ")
    if choose_level_diff == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def the_game():
    # choosing a random number between 1 and 100
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)

    print(f"Psst, the correct answer is {answer}")


    turns = set_difficulty()

    # repeat the guessing function if the user gets it wrong
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number")
        # let the user guess a number
        guess = int(input("Guess a number: "))

        # updating local variable
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("Sorry, you're out of guesses! You lose")
            # exit and ends the function
            return
        elif guess != answer:
            print("Guess again!")


# track the number of turns and reduce by 1 if they get it wrong
the_game()