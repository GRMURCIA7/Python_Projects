# Function to add numbers
def add_numbers(num1, num2):
    return num1 + num2

# Function to subtract numbers
def subtract_numbers(num1, num2):
    return num1 - num2

# Main function
def main():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Calculation
    addition = add_numbers(num1, num2)
    subtraction = subtract_numbers(num1, num2)

    # Results
    print(f"Addition results: {num1} + {num2} = {addition}")
    print(f"Subtraction results: {num1} - {num2} = {subtraction}")

if __name__ == "__main__":
    main()