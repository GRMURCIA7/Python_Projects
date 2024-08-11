class ItemToPurchase:
    # Constructor method
    def __init__(self):
        self.item_name = "none"     # String used for item name
        self.item_price = 0.0       # Float of item price
        self.item_quantity = 0      # Integer to store the number of units of the item

    # Method to print the item cost
    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity  # Calculation of total cost of item
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${total_cost}")  # Display item detail and cost

def main():
    # Create the first instance of the ItemToPurchase class
    item1 = ItemToPurchase()

    # Set the item1 details
    print("Item 1")
    item1.item_name = input("Enter the item name:\n")  # Item name
    item1.item_price = float(input("Enter the item price:\n"))  # Item price
    item1.item_quantity = int(input("Enter the item quantity:\n"))  # Item quantity

    # Create the second instance of the ItemToPurchase class
    item2 = ItemToPurchase()

    # Set the item2 details
    print("\nItem 2")
    item2.item_name = input("Enter the item name:\n")  # Item name
    item2.item_price = float(input("Enter the item price:\n"))  # Item price
    item2.item_quantity = int(input("Enter the item quantity:\n"))  # Item quantity

    # Total cost
    print("\nTOTAL COST")
    item1.print_item_cost()  # Cost for item 1
    item2.print_item_cost()  # Cost for item 2

    # Total cost for both items
    total_cost = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)

    # Display total cost for both items
    print(f"\nTotal: ${total_cost}")

# Call the main function if this script is run
if __name__ == "__main__":
    main()
