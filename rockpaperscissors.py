import random

def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        user_choice = input("Enter rock, paper, or scissors (or 'quit' to stop): ").lower()
        if user_choice == "quit":
            print("Thanks for Playing!")
            break
        
        if user_choice not in choices:
            print("Invalid choice. Try again.")
            continue
        
        print(f"You chose: {user_choice}")
        
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print("You win!")
        else:
            print("You lose!")

rock_paper_scissors()
