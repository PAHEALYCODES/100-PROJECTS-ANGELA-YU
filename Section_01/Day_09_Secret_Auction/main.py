# Day09_SecretAuction.py
# Secret Auction Program

# Import clear function to clear the screen (optional)
from os import system

# Store bidders in a dictionary
bids = {}

# Flag to keep the auction running
auction_going = True

while auction_going:
    # Get user input
    name = input("What is your name? ")
    bid_amount = int(input("What's your bid? $"))
    
    # Store in dictionary
    bids[name] = bid_amount
    
    # Ask if there are other bidders
    should_continue = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if should_continue == "no":
        auction_going = False
    elif should_continue == "yes":
        # Clear the screen for the next bidder (optional)
        system('clear')  # use 'cls' if on Windows
    else:
        print("Invalid input, ending auction.")
        auction_going = False

# Find the winner
highest_bid = 0
winner = ""
for bidder in bids:
    bid = bids[bidder]
    if bid > highest_bid:
        highest_bid = bid
        winner = bidder

# Announce the winner
print(f"The winner is {winner} with a bid of ${highest_bid}")
