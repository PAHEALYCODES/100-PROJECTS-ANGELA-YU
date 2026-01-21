# Day02_TipCalculator.py

# Welcome message
print("Welcome to the Tip Calculator")

# Ask for total bill amount
bill = float(input("What was the total bill? $"))

# Ask for tip percentage
tip_percent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

# Ask how many people will split the bill
people = int(input("How many people to split the bill? "))

# Calculate total tip
total_tip = bill * tip_percent / 100

# Calculate total bill including tip
total_bill = bill + total_tip

# Calculate how much each person should pay
bill_per_person = total_bill / people

# Print the amount per person rounded to 2 decimal places
print(f"Each person should pay: ${bill_per_person:.2f}")
