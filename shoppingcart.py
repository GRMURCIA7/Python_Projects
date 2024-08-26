class ItemToPurchase:     # setting up ItemToPurchase class for each item in shopping cart
    def __init__(self, name="none", description="none", price=0, quantity=0):
        # item attributes
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        
# creating shopping_cart class to manage the shopping cart operations like add, remove, or mod
class shopping_cart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        # shopping cart attributes
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = [] # cart_items will hold the items in the cart
        
    def add_item(self, item_to_purchase):
        # adding items to the cart
        self.cart_items.append(item_to_purchase)
            
    def remove_item(self, item_name):
        # removing items to the cart
        item_removed = False # check if item was found
        for item in self.cart_items:
            if item.name == item_name:
                self.cart_items.remove(item)
                item_removed = True
                break
        if not item_removed:
            print("Item not found in the cart. Nothing removed.") # if item cannot be found print this message
    
    def modify_item(self, item_to_purchase):
        # modifying items in the cart
        item_found = False # check if item was found
        for item in self.cart_items:
            if item.name == item_to_purchase.name:
                item_found = True
                if item_to_purchase.description != "none":
                    item.description = item_to_purchase.description
                if item_to_purchase.price != 0:
                    item.price = item_to_purchase.price
                if item_to_purchase.quantity != 0:
                    item.quantity = item_to_purchase.quantity
                break
        if not item_found:
            print("Item not found in cart. Nothing modified.") # if item cannot be found, printing this message
        
    def get_num_items_in_cart(self):
        # getting the total number of items in the cart
        total_quantity = sum(item.quantity for item in self.cart_items)
        return total_quantity
        
    def get_cost_of_cart(self):
        # getting the total cost of the items in the cart
        total_cost = sum(item.price * item.quantity for item in self.cart_items)
        return total_cost
        
    def print_total(self):
        # printing the total number of items and the total cost of the items in the cart
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY!") # Print this message if no items are in shopping cart
        else:
            print(f"Number Of Items: {self.get_num_items_in_cart()}")
            for item in self.cart_items:
                print(f"{item.name} {item.quantity} @ ${item.price} = ${item.price * item.quantity}")
            print(f"Total: ${self.get_cost_of_cart()}")
                
    def print_descriptions(self):
        # printing the description of the items in the cart
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date} ")
        print("Item Descriptions")
        for item in self.cart_items:
                print(f"{item.name}: {item.description}")
    
def main():
#  creating a shopping cart object in Main Function to use the shopping cart class
    customer_name = input("Enter customer's name: ")
    current_date = input("Enter today's date (example January 1, 2020)")
    cart = shopping_cart(customer_name, current_date)
            
    # displaying shopping cart menu
    while True:
        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")

        option = input("Choose an option: ")
                
        if option == 'a':
            # get item details from the user
            item_name = input("Enter item name: ")
            item_description = input("Enter item description: ")
            item_price = float(input("Enter item price: "))
            item_quantity = int(input("Enter item quantity: "))
                    
            # create an ItemToPurchase and add it to the shopping cart
            item_to_purchase = ItemToPurchase(item_name, item_description, item_price, item_quantity)
            cart.add_item(item_to_purchase)
                    
        elif option == 'r':
            # need item name from the user to remove
            item_name = input("Enter item name to remove: ")
            cart.remove_item(item_name)
                    
        elif option == 'c':
            # get item details to modify
            item_name = input("Enter item name to modify quantity: ")
            new_description = input('Enter the new description (or leave blank to keep current): ') or "none"
            new_price = float(input('Enter the new price (or leave blank to keep current): ') or 0)
            new_quantity = int(input("Enter the new quantity (or leave blank to keep current): ") or 0)
                    
            # create and ItemToPurchase with new details and modifications
            item_to_purchase = ItemToPurchase(item_name, new_description, new_price, new_quantity)
            cart.modify_item(item_to_purchase)
                    
        elif option == 'i':
            # description item output of item in the cart
            cart.print_description()
                    
        elif option == 'o':
            # total cost and details of cart
            cart.print_total()
                    
        elif option == 'q':
            # exit the program
            break
                    
        else:
            # invalid option                
            print("Invalid option. Please try again.")
        
# run the shopping cart script programmed by Garen Murcia
if __name__ == "__main__":
    main()

                
                
                    
                    
    
    
    

    