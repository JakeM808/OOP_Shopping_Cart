
# Instantiate Class and Instance Attributes
class Cart:

    def __init__(self, quantity=1):
        self.cart = {}

     
# Method to add items to cart

    def add_item(self, item, price, quantity):
        if item in self.cart:
            self.cart[item]['quantity'] += quantity
        else:
            self.cart[item] = {'price': price, 'quantity': quantity}

    def remove_item(self, item, quantity):
        if item in self.cart:
            self.cart[item]['quantity'] -= quantity
            if self.cart[item]['quantity'] <= 0:
                del self.cart[item]

    def view_cart(self):
        if not self.cart:
            print("Your shopping cart is empty.")
        else:
            print("Shopping Cart:")
            for item, details in self.cart.items():
                print(f"{item} (Quantity: {details['quantity']}, Price: ${details['price']:.2f} each)")

    def checkout(self, item, price, quantity):
        if not self.cart:
            print("Your shopping cart is empty. No items to checkout.")
        else:
            total_price = sum(price * quantity for item_details in self.cart.values())
            print("\nReceipt:")
            for item, details in self.cart.items():
                print(f"{item} (Quantity: {details['quantity']}, Price: ${details['price']:.2f} each)")
            print(f"Total Price: ${total_price:.2f}")

def main():
    shopping_cart = Cart()

    while True:
        print("\n--- Shop ---")
        print("Add item to cart")
        print("Remove item from cart")
        print("View cart")
        print("Checkout")
        print("Quit")
        choice = input("What would you like to do? Add, remove, view, checkout, or quit ")

        if choice.lower() == 'add':
            item = input("What item would you like to add? ")
            price = float(input("What is the price of this item? "))
            quantity = (input("How many would you like to buy? "))
            shopping_cart.add_item(item, price, quantity)
        elif choice == 'remove':
            item = input("Enter the item name to remove: ")
            quantity = (input("Enter the quantity to remove"))
            shopping_cart.remove_item(item, quantity)
        elif choice == 'view':
            shopping_cart.view_cart()
        elif choice == 'checkout':
            shopping_cart.checkout()
            break
        elif choice == 'quit':
            print("Thank you for using the shopping cart program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()
