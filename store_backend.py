"""
This file is for all of our functions and classes
All of the math etc done on the backend
"""

from mysql.connector import connect

HOST = "localhost"
USER = "root"
PASS = "pass"  # DON'T SAVE YOUR PASSWORD TO GIT, MAKE SURE YOU REMOVE IT BEFORE PUSHING


def login_details(username, password):
    if (username != "AA0001") or (password != "greghard0001"):
        raise ValueError("Your login details were incorrect. Please try again.")
    else:
        pass

# TODO: create a "add new customer"

# TODO: list all active users from the past month


class ShoppingCart:
    # TODO: incorporate with the GUI
    def __init__(self):
        self.items = {}

    def add_item(self, item_name: str,
                 quantity: int,
                 cost: float):
        if not isinstance(item_name, str):
            raise TypeError("Must be string")
        elif not isinstance(quantity, int):
            raise TypeError("Must be int")
        elif not isinstance(cost, float):
            raise TypeError("Must be float")
        elif quantity <= 0:
            raise ValueError("Must be greater than 0")

        if item_name not in self.items.keys():
            self.items[item_name] = [quantity, cost]
        else:
            return

    def remove_item(self, item_name: str,
                    quantity: int):
        assert item_name is not type(str), "Must be string"
        assert quantity is not type(int), "Must be integer"

        # checks to make sure the item is in the shopping cart
        if item_name not in self.items.keys():
            raise AssertionError("This item isn't in your shopping cart")

        # deletes item from shopping cart if quantity specified is greater than amount in cart
        elif self.items[item_name][0] <= quantity:
            self.items.pop(item_name)

        # if quantity specified is less than cart amount, subtract that amount from cart
        elif self.items[item_name][0] > quantity:
            cart_quantity = self.items[item_name][0]
            modified = cart_quantity - quantity
            self.items[item_name][0] = modified

    def get_total_cost(self):
        # TODO: make total cost actually work
        for i in self.items:
            return self.items[i]

# TODO: order parts/vehicles from vendor

# TODO: list all products function

# TODO: list all out-of-stock products function

# TODO: create a finalize order
#   -also create invoice when order is finalized

s1 = ShoppingCart()
s1.add_item("cookies", 4, 5.00)
s1.add_item("bread", 12, 8.40)
print(s1.items)
s1.remove_item("cookies", 2)
s1.remove_item("bread", 12)
print(s1.items)
