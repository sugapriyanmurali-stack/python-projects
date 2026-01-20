class Product:
    def __init__(self, pid, name, price):
        self.pid = pid
        self.name = name
        self.price = price


class ShoppingCart:
    def __init__(self):
        self.cart = []

    def add_product(self, product):
        self.cart.append(product)
        print(f"{product.name} added to cart.")

    def remove_product(self, pid):
        for p in self.cart:
            if p.pid == pid:
                self.cart.remove(p)
                print(f"{p.name} removed from cart.")
                return
        print("Product not found in cart.")

    def view_cart(self):
        if not self.cart:
            print("Cart is empty.")
            return
        total = 0
        print("\nItems in Cart:")
        for p in self.cart:
            print(f"{p.pid} - {p.name} : ₹{p.price}")
            total += p.price
        print("Total Amount: ₹", total)

    def checkout(self):
        if not self.cart:
            print("Cart is empty. Cannot checkout.")
            return
        self.view_cart()
        print("\nOrder placed successfully!")
        self.cart.clear()



products = [
    Product(1, "Mobile", 15000),
    Product(2, "Laptop", 55000),
    Product(3, "Headphones", 2000),
    Product(4, "Keyboard", 1500)
]

cart = ShoppingCart()

while True:
    print("\n--- Online Shopping System ---")
    print("1. View Products")
    print("2. Add to Cart")
    print("3. Remove from Cart")
    print("4. View Cart")
    print("5. Checkout")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("\nAvailable Products:")
        for p in products:
            print(f"{p.pid} - {p.name} : Rs.{p.price}")

    elif choice == 2:
        pid = int(input("Enter product id to add: "))
        for p in products:
            if p.pid == pid:
                cart.add_product(p)
                break
        else:
            print("Invalid product id.")

    elif choice == 3:
        pid = int(input("Enter product id to remove: "))
        cart.remove_product(pid)

    elif choice == 4:
        cart.view_cart()

    elif choice == 5:
        cart.checkout()

    elif choice == 6:
        print("Thank you for shopping!")
        break

    else:
        print("Invalid choice.")
