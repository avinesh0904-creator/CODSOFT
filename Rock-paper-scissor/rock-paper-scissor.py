import random

print("===================================")
print("   ROCK PAPER SCISSORS GAME")
print("===================================")

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

while True:
    user = input("\nEnter Rock, Paper, or Scissors: ").lower()

    if user not in choices:
        print("Invalid choice! Please enter rock, paper, or scissors.")
        continue

    computer = random.choice(choices)

    print("Your Choice     :", user)
    print("Computer Choice :", computer)

    if user == computer:
        print("Result: It's a Tie!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("Result: You Win!")
        user_score += 1
    else:
        print("Result: Computer Wins!")
        computer_score += 1

    print("\nCurrent Score")
    print("You      :", user_score)
    print("Computer :", computer_score)

    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("\n========== FINAL SCORE ==========")
        print("You      :", user_score)
        print("Computer :", computer_score)

        if user_score > computer_score:
            print("Overall Winner: You!")
        elif computer_score > user_score:
            print("Overall Winner: Computer!")
        else:
            print("Overall Result: It's a Tie!")

        print("\nThank you for playing!") 
        break