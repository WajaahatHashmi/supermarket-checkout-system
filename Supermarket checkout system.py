class Supermarket:
    def __init__(self):
        self.products = {
            "apple":     {"price": 2.0, "stock": 50},
            "bread":     {"price": 3.5, "stock": 30},
            "milk":      {"price": 4.0, "stock": 20},
            "chocolate": {"price": 1.5, "stock": 40}
        }
        self.cart = {}
    
    def browse_products(self):
        print('\n-----Available Products-----')
        for name,info in self.products.items():
            print("{0}: ${1:.2f} (Stock: {2})".format(name.capitalize(),info['price'],info['stock']))
    
    def add_to_cart(self, item, quantity):
        item = item.lower()
        if item in self.products:
            if self.products[item]["stock"] >= quantity:
                if item in self.cart:
                    self.cart[item] += quantity
                else:
                    self.cart[item] = quantity
                self.products[item]["stock"] -= quantity
                print(f"Added {quantity}x {item} to cart.")
            else:
                print(f"Only {self.products[item]['stock']} in stock.")
        else:
            print("Item not found.")

    def remove_from_cart(self, item):
        item = item.lower()
        if item in self.cart:
            self.products[item]["stock"] += self.cart[item]
            del self.cart[item]
            print(f"Removed {item} from cart.")
        else:
            print("Item not in cart.")
    
    def view_cart(self):
        if self.cart:
            print("\n-----Your cart-----")
            for item, qty in self.cart.items():
                price = self.products[item]['price']
                print("{0}: {1} x ${2:.2f} = ${3:.2f}".format(item.capitalize(),qty,price,qty*price))
        else:
            print("Cart is empty")

    def calculate_total(self):
        total = 0
        for item,qty in self.cart.items():
            total += self.products[item]["price"] * qty
        return total

    def apply_discount(self,total):
        if total > 50:
            total *= 0.85
        return total
    
    def checkout(self):
        if self.cart:
            self.view_cart()
            raw_total = self.calculate_total()
            final_total = self.apply_discount(raw_total)
            print("\nYour subtotal is  ${0:.2f}".format(raw_total))
            if final_total < raw_total:
                print("Discount:  -${0:.2f}".format(raw_total - final_total))
            print("Total:  ${0:.2f}".format(final_total))
            print("\nThank you for shopping with us!")
            self.cart = {}
        else:
            print("Your cart is empty.")

    def run(self):
        print("\n**Welcome to the Supermarket**")  
        while True:
            print("\n----------Menu----------")
            print("1. Browse Products")
            print("2. Add item to the cart")
            print("3. Remove item from cart")
            print("4. View cart")
            print("5. Checkout")
            print("6. Exit")

            choice = input("Enter your option: ")

            if choice == '1':
                self.browse_products()
            elif choice == '2':
                item = input("Enter the name of the item: ")
                qty = int(input("Enter the quantity: "))
                self.add_to_cart(item,qty)
            elif choice == '3':
                if len(self.cart) == 0:
                    print("\nCart is empty")
                    self.browse_products()
                else:
                    item = input("Enter item you want to remove: ")
                    self.remove_from_cart(item)
            elif choice == '4':
                self.view_cart()
            elif choice == '5':
                self.checkout()
                break
            elif choice == '6':
                print("Goodbye!!")
                break
            else:
                print("Invalid option, Try agsin ")

shop = Supermarket()
shop.run()