# Simple calculator program

# Function to add two numbers
def add(num1, num2):
    return num1 + num2

# Function to subtract two numbers
def subtract(num1, num2):
    return num1 - num2

# Function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2

# Function to divide two numbers
def divide(num1, num2):
    if num2 == 0:
        print("Error: Division by zero")
        return None
    else:
        return num1 / num2

# Main program loop(This a way of keeping the program constantly running until the loop is broken or exited)
while True:
    # Get user input for operation and numbers
    operation = input("Enter operation (+, -, *, /): ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Perform arithmetic operation and display result
    if operation == "+":
        print("Result: ", add(num1, num2))
    elif operation == "-":
        print("Result: ", subtract(num1, num2))
    elif operation == "*":
        print("Result: ", multiply(num1, num2))
    elif operation == "/":
        result = divide(num1, num2)
        if result != None:
            print("Result: ", result)
    else:
        print("Invalid operation")

    # Ask user if they want to perform another calculation and break is called to exit the loop
    choice = input("Perform another calculation? (y/n): ")
    if choice == "n":
        break
