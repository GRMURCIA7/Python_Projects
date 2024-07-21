# Function to multiply numbers
def multiply_numbers(num1, num2):
    return num1 * num2

# Function to divide numbers
def divide_numbers(num1, num2):
    if num2 == 0:
        return "Divide by zero not allowed."
    else:
        return num1 / num2

# Main Function
def main():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    multiplication = multiply_numbers(num1, num2)
    division = divide_numbers(num1, num2)

    print(f"Multiplication result: {num1} * {num2} = {multiplication}")
    print(f"Division result: {num1} / {num2} = {division}")

if __name__ == "__main__":
    main()
