# Day10_Calculator.py

# Define basic math functions
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

# Dictionary mapping symbols to functions
operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

# Take user input
num1 = float(input("Enter first number: "))
for symbol in operations:
    print(symbol)
operation_symbol = input("Pick an operation: ")
num2 = float(input("Enter next number: "))

# Perform calculation
calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)

# Show result
print(f"{num1} {operation_symbol} {num2} = {answer}")
i