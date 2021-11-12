import random
print("Welcome to Rock, Paper, Scissors Game")

while True:
    print("Do you want to play?")
    play_again = input("(y / n) : " )
    if play_again == "y":
        user_action = input("Enter a choice (rock, paper, scissors) :")
        if user_action == "rock" or user_action == "paper" or user_action == "scissors":
            possible_actions = ["rock", "paper", "scissors"]
            computer_action = random.choice(possible_actions)
            print(f"You chose {user_action}, computer chose {computer_action}.\n")
            if user_action == computer_action:
                print(f"Both players selected {user_action}. It's a tie!")
            elif user_action == "rock":
                if computer_action == "scissors":
                    print("Rock smashes scissors! You win!")
                else:
                     print("Paper covers rock! You lose.")
            elif user_action == "paper":
                if computer_action == "rock":
                    print("Paper covers rock! You win!")
                else:
                    print("Scissors cuts paper! You lose.")
            elif user_action == "scissors":
                if computer_action == "paper":
                    print("Scissors cuts paper! You win!")
                else:
                    print("Rock smashes scissors! You lose.")
        else:
            print("Invalid choice")
    else:
        print("Thankyou! Game exit")
        break



