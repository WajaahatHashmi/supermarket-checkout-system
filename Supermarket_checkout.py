import json
import os

CART_FILE = "cart_data.json"


class Supermarket:
    def __init__(self):
        self.products = {
            "apple":     {"price": 2.0, "stock": 50},
            "bread":     {"price": 3.5, "stock": 30},
            "milk":      {"price": 4.0, "stock": 20},
            "chocolate": {"price": 1.5, "stock": 40}
        }
        self.cart = self.load_cart()
        # Keep stock consistent with any items restored from a saved cart
        for item, qty in self.cart.items():
            if item in self.products:
                self.products[item]["stock"] -= qty

    # ---------- Persistence ----------
    def load_cart(self):
        if os.path.exists(CART_FILE):
            try:
                with open(CART_FILE, "r") as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                return {}
        return {}

    def save_cart(self):
        with open(CART_FILE, "w") as f:
            json.dump(self.cart, f)

    # ---------- Core features ----------
    def browse_products(self):
        print("\n-----Available Products-----")
        for name, info in self.products.items():
            print("{0}: ${1:.2f} (Stock: {2})".format(
                name.capitalize(), info["price"], info["stock"]))

    def add_to_cart(self, item, quantity):
        item = item.lower().strip()

        if quantity <= 0:
            print("Quantity must be a positive number.")
            return

        if item not in self.products:
            print("Item not found.")
            return

        if self.products[item]["stock"] < quantity:
            print(f"Only {self.products[item]['stock']} in stock.")
            return

        self.cart[item] = self.cart.get(item, 0) + quantity
        self.products[item]["stock"] -= quantity
        self.save_cart()
        print(f"Added {quantity}x {item} to cart.")

    def remove_from_cart(self, item):
        item = item.lower().strip()
        if item in self.cart:
            self.products[item]["stock"] += self.cart[item]
            del self.cart[item]
            self.save_cart()
            print(f"Removed {item} from cart.")
        else:
            print("Item not in cart.")

    def view_cart(self):
        if self.cart:
            print("\n-----Your cart-----")
            for item, qty in self.cart.items():
                price = self.products[item]["price"]
                print("{0}: {1} x ${2:.2f} = ${3:.2f}".format(
                    item.capitalize(), qty, price, qty * price))
        else:
            print("Cart is empty")

    def calculate_total(self):
        return sum(self.products[item]["price"] * qty
                   for item, qty in self.cart.items())

    def apply_discount(self, total):
        # Tiered discount instead of a single hardcoded cutoff
        if total > 100:
            return total * 0.80
        elif total > 50:
            return total * 0.85
        elif total > 25:
            return total * 0.95
        return total

    def checkout(self):
        if not self.cart:
            print("Your cart is empty.")
            return

        self.view_cart()
        raw_total = self.calculate_total()
        final_total = self.apply_discount(raw_total)

        print("\nYour subtotal is  ${0:.2f}".format(raw_total))
        if final_total < raw_total:
            print("Discount:  -${0:.2f}".format(raw_total - final_total))
        print("Total:  ${0:.2f}".format(final_total))
        print("\nThank you for shopping with us!")

        self.cart = {}
        self.save_cart()

    # ---------- Input helpers ----------
    def prompt_quantity(self):
        raw = input("Enter the quantity: ").strip()
        if not raw.isdigit():
            print("Please enter a whole number.")
            return None
        return int(raw)

    # ---------- Main loop ----------
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

            choice = input("Enter your option: ").strip()

            if choice == "1":
                self.browse_products()
            elif choice == "2":
                item = input("Enter the name of the item: ")
                qty = self.prompt_quantity()
                if qty is not None:
                    self.add_to_cart(item, qty)
            elif choice == "3":
                if not self.cart:
                    print("\nCart is empty")
                    self.browse_products()
                else:
                    item = input("Enter item you want to remove: ")
                    self.remove_from_cart(item)
            elif choice == "4":
                self.view_cart()
            elif choice == "5":
                self.checkout()
                break
            elif choice == "6":
                print("Goodbye!!")
                break
            else:
                print("Invalid option, try again.")


if __name__ == "__main__":
    shop = Supermarket()
    shop.run()
