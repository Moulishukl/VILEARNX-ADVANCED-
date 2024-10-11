# Function for addition
def add(x, y):
    return x + y

# Function for subtraction
def subtract(x, y):
    return x - y

# Function for multiplication
def multiply(x, y):
    return x * y

# Function for division
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Main function to run the calculator
def calculator():
    print("Simple Calculator")
    
    # Get input from the user
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Please enter numbers only.")
        return
    
    # Display the operation choices
    print("\nChoose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    # Get the user's choice
    choice = input("\nEnter choice (1/2/3/4): ")
    
    # Perform the selected operation
    if choice == '1':
        print(f"\nResult: {num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"\nResult: {num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"\nResult: {num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        result = divide(num1, num2)
        print(f"\nResult: {num1} / {num2} = {result}")
    else:
        print("\nInvalid choice! Please select a valid operation.")

# Run the calculator
calculator()