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
        # TODO: make this connect to sql database
        pass

# TODO: create a "add new customer"

# TODO: list all active users from the past month

# TODO: make a shopping cart
#   -functionality to add/remove items
#   -track user id or name within the order

# TODO: order parts/vehicles from vendor

# TODO: list all products function

# TODO: list all out-of-stock products function

# TODO: create a finalize order
#   -also create invoice when order is finalized
