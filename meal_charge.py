# Moduale 3, Part 1 Calculatiing meal charge 

# Entering the charge for the meal
meal_charge = float(input("Enter the cost of the meal: $"))

# Calculating the tip for the meal charge at 18% gratuity
tip = meal_charge * 0.18

# Calculating the sales tax at 7% for the meal charge
sales_tax = meal_charge * 0.07

 # Calculating the total cost for meal charge with 18% gratuity and 7% sales tax
 
total_cost =  meal_charge + tip + sales_tax
 
 # Showing the itemized cost per item and providing the total
print(f"\nMeal Charge: ${meal_charge:.2f}")
print(f"Tip (18%): ${tip:.2f}")
print(f"Sales Tax (7%): ${sales_tax:.2f}")
print(f"Total Price: ${total_cost:.2f}")
