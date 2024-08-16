def calculate_points(num_books):
    """Calculate the points awarded based on the number of books purchased."""
    if num_books == 0:
        return 0
    elif num_books == 2:
        return 5
    elif num_books == 4:
        return 15
    elif num_books == 6:
        return 30
    elif num_books >= 8:  # Adjusted to include 8 or more books
        return 60
    else:
        print("Invalid number of books. Points will remain at zero.")
        return 0 

def main():
    total_points = 0  # Total points starts at zero
    
    num_books = int(input("Enter the number of books purchased this month: "))  # Ask for the number of books
    
    total_points += calculate_points(num_books)  # Update total points with the points earned
    
    # Print the points awarded based on purchase
    print(f"You have earned {total_points} points this month.")
    print(f"Your total points earned as of now are {total_points}")

if __name__ == "__main__":
    main()
