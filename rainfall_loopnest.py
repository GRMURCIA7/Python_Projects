def get_rainfall_data():
    """
    Get rainfall data from the user for a specified number of years and months.
    Returns the total inches of rainfall and the total number of months.
    """
    num_years = int(input("Enter number of years: "))  # Input the number of years to calculate
    
    # Variables to track total rainfall and total months
    total_inches_of_rainfall = 0
    total_months = 0
    
    # Outer loop runs once for each year
    for year in range(1, num_years + 1):
        print(f"\nYear {year}:")
        
        # Inner loops run over each month
        for month in range(1, 13):
            # Input the inches of rainfall
            rainfall = float(input(f"Enter the total inches of rainfall for month {month}: "))
            
            # Adding to total rainfall
            total_inches_of_rainfall += rainfall
            
            # Month increment
            total_months += 1
    
    return total_inches_of_rainfall, total_months

def calculate_average_rainfall(total_inches_of_rainfall, total_months):
    """
    Calculates the average rainfall based on the total inches of rainfall and total months.
    Returns the average rainfall per month.
    """
    average_rainfall = total_inches_of_rainfall / total_months
    return average_rainfall

def main():
    total_inches, total_months = get_rainfall_data()
    average_rainfall = calculate_average_rainfall(total_inches, total_months)
    
    # Print results
    print("\nResults:")
    print(f"Total number of months: {total_months}")
    print(f"Total inches of rainfall: {total_inches:.2f}")
    print(f"Average rainfall per month: {average_rainfall:.2f} inches")

if __name__ == "__main__":
    main()
