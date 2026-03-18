class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        return f"Item added to cart: {item.name}"

    def show_items(self):
        output = ["Items in the cart:"]
        for item in self.items:
            output.append(f"- {item.name}")
        return "\n".join(output)
    
    def remove_item(self, item):
        self.items.remove(item)  # still crashes if not found (keep it as is)
        return f"{item.name} removed from the cart."

# Creating new objects from Item class
item1 = Item("cola", 3000)
item2 = Item("sprite", 3000)
item3 = Item("fanta", 3000)

# initializing/creating the ShoppingCart
cart1 = ShoppingCart()

# Adding new items into the shopping cart
cart1.add_item(item1)
cart1.add_item(item2)
cart1.add_item(item3)

# Showing all items in the cart
cart1.show_items()

# Removing the item: cola from the cart
cart1.remove_item(item1)

# Re-showing all the items in the cart, to confirm the cola was removed.
cart1.show_items()


