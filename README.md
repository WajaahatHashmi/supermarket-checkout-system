# Supermarket Checkout System

A terminal-based supermarket checkout program written in Python. Browse products, manage a shopping cart, and check out with automatic tiered discounts. The cart is saved to disk, so it survives closing the program.

## Features

- **Browse products** with live prices and stock levels
- **Add and remove items**, with stock updating in real time
- **Persistent cart** saved to `cart_data.json` and restored on the next run
- **Tiered discounts** applied automatically at checkout
- **Input validation** so bad input never crashes the program
- **Itemised receipt** showing subtotal, discount, and final total

## Getting started

### Requirements

- Python 3.6 or newer (uses f-strings)
- No external packages. Only the standard library (`json`, `os`) is used.

### Run it

```bash
git clone https://github.com/WajaahatHashmi/supermarket-checkout-system.git
cd supermarket-checkout-system
python3 supermarket_checkout.py
```

> **Note:** the cart is saved to a local file, so this needs to run on your own machine. Browser-based compilers that block file access won't support the saved cart.

## Usage

```
**Welcome to the Supermarket**

----------Menu----------
1. Browse Products
2. Add item to the cart
3. Remove item from cart
4. View cart
5. Checkout
6. Exit
```

Example session:

```
Enter your option: 2
Enter the name of the item: apple
Enter the quantity: 30
Added 30x apple to cart.

Enter your option: 5

-----Your cart-----
Apple: 30 x $2.00 = $60.00

Your subtotal is  $60.00
Discount:  -$9.00
Total:  $51.00

Thank you for shopping with us!
```

## Discount tiers

| Subtotal | Discount |
|----------|----------|
| Over $25 | 5% |
| Over $50 | 15% |
| Over $100 | 20% |

## Version history

This repo is tagged so you can compare the original with the upgraded version.

| Version | Description |
|---------|-------------|
| `v1` | Original version: basic cart, single 15% discount over $50 |
| `v2` | Upgraded version (current) |

**What changed from v1 to v2**

- Quantity input is validated: letters, zero, and negative numbers are rejected instead of crashing the program or corrupting stock
- Cart persists between runs using JSON file storage
- Stock is kept consistent when a saved cart is restored
- Single discount rule replaced with three tiers
- Flatter control flow using early returns instead of deeply nested `if/else`
- `if __name__ == "__main__":` guard so the class can be imported and tested
- Whitespace in user input is trimmed, and a typo in the menu message is fixed

To see the exact differences, open the [v1 to v2 comparison](https://github.com/WajaahatHashmi/supermarket-checkout-system/compare/v1...v2).

## Project structure

```
supermarket-checkout-system/
├── supermarket_checkout.py   # Main program
├── .gitignore                # Excludes cart_data.json
└── README.md
```

## Roadmap

- [ ] Load products from a `products.json` file instead of hardcoding them
- [ ] Unit tests for discounts and cart logic
- [ ] Save a receipt to a text file at checkout
- [ ] Graphical interface

## Author

Wajaahat Hashmi ([@WajaahatHashmi](https://github.com/WajaahatHashmi))
