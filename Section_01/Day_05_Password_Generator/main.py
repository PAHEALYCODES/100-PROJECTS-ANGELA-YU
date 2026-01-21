# Day05_PasswordGenerator.py
import random  # Import random module to select random characters

# Define character sets
letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!@#$%^&*()'

# Welcome message
print("Welcome to the PyPassword Generator!")

# Ask user for number of letters, symbols, and numbers
nr_letters = int(input("How many letters? "))
nr_symbols = int(input("How many symbols? "))
nr_numbers = int(input("How many numbers? "))

# Create password list
password_list = []

# Add random letters
for char in range(nr_letters):
    password_list.append(random.choice(letters))

# Add random symbols
for char in range(nr_symbols):
    password_list.append(random.choice(symbols))

# Add random numbers
for char in range(nr_numbers):
    password_list.append(random.choice(numbers))

# Shuffle the password list
random.shuffle(password_list)

# Join list to create password string
password = ''.join(password_list)

# Print the generated password
print(f"Your password is: {password}")
