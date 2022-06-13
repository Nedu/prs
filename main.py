import random

possible_options = ["R", "P", "S"]
user_input = False


while user_input == False:
    user_input = input("Enter a choice (R, P, S): ")
    computer_choice = random.choice(possible_options)
    print(f"\nPlayer ({user_input}): Computer ({computer_choice})\n")

    if user_input == computer_choice:
        print(f"Both players selected {user_input}. It's a tie! Play again!")
        user_input = False
    elif user_input == "R":
        if computer_choice == "scissors":
            print("Player wins!")
        else:
            print("Computer wins!")
    elif user_input == "P":
        if computer_choice == "rock":
            print("Player wins!")
        else:
            print("Computer wins!")
    elif user_input == "S":
        if computer_choice == "paper":
            print("Player wins!")
        else:
            print("Computer wins!")
    else:
        print("Error! Please choose a valid option!")
        user_input = False
