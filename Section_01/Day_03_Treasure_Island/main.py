 # Day03_TreasureIsland.py

# Welcome message
print("Welcome to Treasure Island.")

# First choice at the crossroad
choice1 = input("You're at a cross road. Where do you want to go? Type 'left' or 'right'\n").lower()

# Check first choice
if choice1 == "left":
    # Second choice at the lake
    choice2 = input("You've come to a lake. Type 'wait' to wait for a boat or 'swim' to swim across\n").lower()
    if choice2 == "wait":
        # Third choice: doors
        choice3 = input("You arrive at three doors: red, yellow, blue. Which one?\n").lower()
        if choice3 == "yellow":
            print("You found the treasure! You win!")
        elif choice3 == "red":
            print("Burned by fire. Game over.")
        elif choice3 == "blue":
            print("Eaten by beasts. Game over.")
        else:
            print("Game over.")
    else:
        print("Attacked by trout. Game over.")
else:
    print("Fall into a hole. Game over.")
