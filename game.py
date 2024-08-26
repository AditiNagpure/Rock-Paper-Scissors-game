import random

def game():
    while True:
        user = input("Enter your choice (rock/paper/scissors) or 'q' to quit: ").lower()
        if user == 'q':
            break

        if user not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please enter rock, paper, or scissors.")
            continue

        choices = ['rock', 'paper', 'scissors']
        computer = random.choice(choices)

        print(f"\nYou chose: {user}")
        print(f"Computer chose: {computer}\n")

        if user == computer:
            print(f"Both players selected {user}. It's a tie!")
        elif user == 'rock':
            if computer == 'scissors':
                print("Rock smashes scissors! You win!")
            else:
                print("Paper covers rock! You lose.")
        elif user == 'paper':
            if computer == 'rock':
                print("Paper covers rock! You win!")
            else:
                print("Scissors cuts paper! You lose.")
        elif user == 'scissors':
            if computer == 'paper':
                print("Scissors cuts paper! You win!")
            else:
                print("Rock smashes scissors! You lose.")

game()
