import random

COLORS = ["R", "G", "B", "Y", "W", "O"]
NUM_TRIES = 10
CODE_LENGTH = 4

def generate_code():
    code = []
    # using _ in the loop refers to iteration being n amount of times without using an iteration counter
    for _ in range(CODE_LENGTH):
        color = random.choice(COLORS)
        code.append(color)
    return code

#code = generate_code()


def guess_code():

    while True:
        guess = input("Guess: ").upper().split(" ") # split creates elements in a list --> "G G G" -> ["G", "G", "G"]

        if len(guess) != CODE_LENGTH:
            print(f"You must guess {CODE_LENGTH} colors.")
            continue

        for color in guess:
            if color not in COLORS:
                print(f"Invalid color. {color}. Try again.")
                break
        else:
            break

    return guess

def check_code(guess, real_code):
    color_counts = {}
    correct_pos = 0
    incorrect_pos = 0

    for color in real_code:
        if color not in color_counts:
            color_counts[color] = 0 # making color_counts available for incrementation by setting it to 0 first
        color_counts[color] += 1

    for guess_color, real_color in zip(guess, real_code): # zip is going to combine arguments into tuples
        if guess == real_color:
            correct_pos += 1
            color_counts[guess_color] -= 1

    # ["G", "O", "O", "O"] real
    # ["G", "G", "W", "W"]

    for guess_color, real_color in zip(guess, real_code):
        if guess_color in color_counts and color_counts[guess_color] > 0:
            incorrect_pos += 1
            color_counts[guess_color] -= 1

    return correct_pos, incorrect_pos

def game():
    print(f"Welcome to Color Game! You have {NUM_TRIES} tries to guess the code...")
    print("The valid colors are,", *COLORS)
    code = generate_code()
    for attempts in range(1, NUM_TRIES + 1):
        # ask user to guess the code
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)

        if correct_pos == CODE_LENGTH:
            print(f"You guess the code in {attempts} tries.")
            break

        print(f"Correct positions: {correct_pos}, Incorrect positions: {incorrect_pos}")
    else:
        print("You ran out of tries, the code was:", *code) # print each individual element from the list

if __name__ == "__main__": # directly runs the python file
    game()


