class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"Item added to cart: {item.name}")

    def show_items(self):
        print("Items in the cart:")
        for item in self.items:
            print("-", item.name)
    
    def remove_item(self, item):
        self.items.remove(item)
        print(item.name, "removed from the cart.")


item1 = Item("cola", 3000)
item2 = Item("sprite", 3000)
item3 = Item("fanta", 3000)

cart1 = ShoppingCart()

cart1.add_item(item1)
cart1.add_item(item1)
cart1.add_item(item1)

cart1.show_items()

cart1.remove_item(item1)

cart1.show_items()


