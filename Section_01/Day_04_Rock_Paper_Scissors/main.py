# Day04_RockPaperScissors.py
import random  # Import random module to generate computer's choice

# Welcome message
print("Welcome to Rock, Paper, Scissors!")

# Ask user to choose 0,1,2 for Rock, Paper, Scissors
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# List of choices for reference
choices = ["Rock", "Paper", "Scissors"]

# Computer randomly picks a choice
computer_choice = random.randint(0,2)

# Print both choices
print(f"You chose: {choices[user_choice]}")
print(f"Computer chose: {choices[computer_choice]}")

# Determine the winner
if user_choice == computer_choice:
    print("It's a draw!")
elif (user_choice == 0 and computer_choice == 2) or \
     (user_choice == 1 and computer_choice == 0) or \
     (user_choice == 2 and computer_choice == 1):
    print("You win!")
else:
    print("You lose!")
