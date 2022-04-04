"""
This file is for all of our functions and classes
All of the math etc done on the backend
"""

# TODO: -enter user_details(username n password),
#  -order parts or products from the vendor
#  -add or remove product from cart
#  -invoice creation
#  -input customer data (for new customer)


def login_details(username, password):
    if (username != "AA0001") or (password != "greghard0001"):
        raise ValueError("Your login details were incorrect. Please try again.")
    else:
        # TODO: make this connect to sql database
        pass
