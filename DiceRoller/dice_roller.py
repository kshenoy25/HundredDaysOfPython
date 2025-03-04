import random

while True:
    try:
        dice_roll_choice = input("Roll the dice (y/n): ").lower()
        if dice_roll_choice == "y":
            # generate two random numbers
            die1 = random.randint(1, 6)
            die2 = random.randint(1, 6)
            print(f"{die1}, {die2}")

        elif dice_roll_choice == "n":
            print("Thanks for playing!")
            break

        else:
            raise ValueError("Invalid input! Please enter 'y' to roll the dice or 'n' to exit.")

    except ValueError as e:
        print(f"Error {e}")
