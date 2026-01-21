 # Day07_Hangman.py
import random

# List of possible words
word_list = ["python", "hangman", "program"]

# Randomly choose a word
chosen_word = random.choice(word_list)

# Create display with underscores
display = ["_"] * len(chosen_word)

# Set number of lives
lives = 6

# Game loop
while "_" in display and lives > 0:
    guess = input("Guess a letter: ").lower()

    # Check guessed letter and update display
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess

    # If guess is wrong, lose a life
    if guess not in chosen_word:
        lives -= 1
        print(f"Wrong! Lives left: {lives}")

    # Show current state
    print(display)

# Check win or lose
if "_" not in display:
    print("You win!")
else:
    print(f"You lose! The word was {chosen_word}")
