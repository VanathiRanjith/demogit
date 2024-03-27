class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

class ShoppingCart:
    def __init__(self):
        self.items = []
        self.add_initial_items()

    def add_initial_items(self):
        biscuits = Product("Biscuits", 20.5)
        cereals = Product("Cereals", 90)
        chicken = Product("Chicken", 100)
        self.items.append(CartItem(biscuits, 5))
        self.items.append(CartItem(cereals, 10))
        self.items.append(CartItem(chicken, 20))

    def add_item(self, product, quantity):
        self.items.append(CartItem(product, quantity))

    def calculate_total(self):
        total = 0
        # Exclude initial items from total calculation
        for item in self.items[3:]:
            total += item.product.price * item.quantity
        return total

    def view_cart(self):
        if len(self.items) > 3:
            print("{:<5} {:<15} {:<10} {:<10}".format("Sr.No", "Item", "Quantity", "Total Cost"))
            for i, item in enumerate(self.items[3:], 1):
                item_total = item.product.price * item.quantity
                print("{:<5} {:<15} {:<10} ${:<10.2f}".format(i, item.product.name, item.quantity, item_total))
            print("Total: ${:.2f}".format(self.calculate_total()))

def calculate_delivery_charge(distance):
    if distance <= 15:
        return 50
    elif 15 < distance <= 30:
        return 100
    else:
        return 0

def main():
    cart = ShoppingCart()
    print("{:<5} {:<15} {:<10} {:<10}".format("Sr.No", "Item", "Quantity", "Cost/Item"))
    print("{:<5} {:<15} {:<10} {:<10}".format("1", "Biscuits", "5", "20.5"))
    print("{:<5} {:<15} {:<10} {:<10}".format("2", "Cereals", "10", "90"))
    print("{:<5} {:<15} {:<10} {:<10}".format("3", "Chicken", "20", "100"))

    first_item_added = False

    while True:
        cart.view_cart()
        choice = input("\nWhat do you want to purchase? (1. Biscuits, 2. Cereals, 3. Chicken, 4. Checkout, 5. Exit): ")

        if choice == '1':
            quantity = int(input("How many Biscuits packets you want to purchase: "))
            if quantity <= 5:
                product = Product("Biscuits", 20.5)
                cart.add_item(product, quantity)
                print("Biscuits added to cart.")
                first_item_added = True
            else:
                print("Invalid quantity. Available quantity of biscuits is 5.")

        elif choice == '2':
            quantity = int(input("How many Cereals packets you want to purchase: "))
            if quantity <= 10:
                product = Product("Cereals", 90)
                cart.add_item(product, quantity)
                print("Cereals added to cart.")
                first_item_added = True
            else:
                print("Invalid quantity. Available quantity of cereals is 10.")

        elif choice == '3':
            quantity = int(input("How many Chicken you want to purchase: "))
            if quantity <= 20:
                product = Product("Chicken", 100)
                cart.add_item(product, quantity)
                print("Chicken added to cart.")
                first_item_added = True
            else:
                print("Invalid quantity. Available quantity of chicken is 20.")

        elif choice == '4':
            if first_item_added:
                total = cart.calculate_total()
                print("Total cost of items in cart: ${:.2f}".format(total))
                name = input("Enter your name: ")
                address = input("Enter your address: ")
                distance = int(input("Enter the distance from store 5/10/15/30: "))
                delivery_charge = calculate_delivery_charge(distance)
                print("\nDelivery charge: ${:.2f}".format(delivery_charge))
                total_cost = total + delivery_charge
                print("\n---------- Bill -------------")
                cart.view_cart()
                print("Total items cost: ${:.2f}".format(total))
                print("Total Bill Amount: Total items + Delivery charge is: ${:.2f}".format(total_cost))
                print("Name:", name)
                print("Address:", address)
                print("Have a nice day!!")
                break
            else:
                print("Please add items to your cart before checkout.")

        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
