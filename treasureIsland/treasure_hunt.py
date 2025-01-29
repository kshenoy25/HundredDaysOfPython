from random import choice

print("Welcome to Treasure Island!")
print("Your mission is to find the treasure!")
choice1 = input('You\'re at a crossroad, where would you like to go? '
                ' Type "Left" or "Right".\n').lower()

if choice1 == "left":
    choice2 = input('You\'ve come to a lake and there is an island in the middle. '
                    'Type "wait" to wait for a boat. '
                    'Type "swim" to swim towards the island.').lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. There is a house with some doors. "
                           "One is red. The other is blue and the third one is yellow. "
                           "Which colour do you choose?").lower()

        if choice3 == "blue":
            print("You have been caught by a man in a frightful mask."
                  " He cuts open your head with a machete. Game Over.")
        elif choice3 == "yellow":
            print("You have found it! The treasure full of gold and jewels! You Win!")
        elif choice3 == "red":
            print("You fall into a pit of venomous cobras. Game Over!")
        else:
            print("That door does not exist."
                  " A trap is triggered and the house is not flooded with toxic fumes and you die."
                  " Game Over!")


    else:
        print("You got attacked by a giant alligator!")


else:
    print("A giant spider has appeared and taken you for its meal. Game Over.")
