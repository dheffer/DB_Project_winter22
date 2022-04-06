"""
This file is for all of our functions and classes
All of the math etc done on the backend
"""

from mysql.connector import connect

HOST = "localhost"
USER = "root"
PASS = "pass"  # DON'T SAVE YOUR PASSWORD TO GIT, MAKE SURE YOU REMOVE IT BEFORE PUSHING

# thing below was a test; might use later
"""def login_details(username, password):
    if (username != "AA0001") or (password != "greghard0001"):
        raise ValueError("Your login details were incorrect. Please try again.")
    else:
        pass"""


# TODO: create a "add new customer"
def add_new_customer(name, email, address, phone, vehic_license):
    with connect(host=HOST, user=USER, password=PASS) as mysql_connection:
        with mysql_connection.cursor() as cursor:
            access_database = "USE generic_vehicle_merchant;"
            query = f"""INSERT INTO customer(
            cust_name, cust_email, cust_address, cust_phone, cust_license)
            VALUES ("{name}", "{email}", "{address}", {phone}, {vehic_license});"""
            cursor.execute(access_database)
            cursor.execute(query)
            mysql_connection.commit()
            # TODO: make it so if a name, email, etc are in the database
            #  then don't add the customer again?

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
            self.items.update({item_name: [quantity, cost]})
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
        maths = 0
        for i in self.items:
            maths += float(self.items[i][0]) * float(self.items[i][1])
        return round(maths, 2)


# TODO: order parts/vehicles from vendor
#  unsure if this is finished, please update if not, else delete this to-do thing
def update_from_vendor(quantity: int, product_name: str):
    # Create connection
    with connect(host=HOST, user=USER, password=PASS) as mysql_connection_object:

        # Create cursor
        with mysql_connection_object.cursor() as mysql_cursor:
            # Create SQL statement
            update_statement = f"""USE generic_vehicle_merchant;"""
            update_statement2 = f"""UPDATE products
                                    SET quantity = {quantity}
                                    WHERE product_name = '{product_name}';"""
            # Execute the statement
            mysql_cursor.execute(update_statement)
            mysql_cursor.execute(update_statement2)
            # Commit the change
            mysql_connection_object.commit()


def get_all_products():
    # Create connection
    with connect(host=HOST, user=USER, password=PASS) as mysql_connection_object:
        # Create cursor
        with mysql_connection_object.cursor() as mysql_cursor:
            # Create SQL statement
            update_statement = f"""USE generic_vehicle_merchant;"""
            update_statement2 = f"""SELECT product_name
                                    FROM `generic_vehicle_merchant`.`products`;"""
            # Execute the statement
            mysql_cursor.execute(update_statement)
            mysql_cursor.execute(update_statement2)
            for row in mysql_cursor:
                print(row)
            # Commit the change
            mysql_connection_object.commit()


print(get_all_products())


def list_out_of_stock_products():
    """
    :return: returns a list of all out of stock products, useful to
     know when to order more
    """
    # TODO: incorporate with GUI
    with connect(host=HOST, user=USER, password=PASS) as mysql_connection:
        with mysql_connection.cursor() as mysql_cursor:
            access_database = "USE generic_vehicle_merchant;"
            query = f"""SELECT * FROM products
                WHERE quantity = {10}
                """
            mysql_cursor.execute(access_database)
            mysql_cursor.execute(query)
            out_of_stock = mysql_cursor.fetchall()
            list_of_no_stock = []
            for no_stock in out_of_stock:
                list_of_no_stock.append(no_stock[0:5])

    return list_of_no_stock

# TODO: create a finalize order
#   -also create invoice when order is finalized
#   -will need to reference ShoppingCart class to remove items from database


"""
TEST CASES FOR CODE BELOW
"""
s1 = ShoppingCart()
s1.add_item("cookies", 4, 5.00)
s1.add_item("bread", 12, 8.40)
print("-" * 50)
print(s1.items)
print(s1.get_total_cost())
print(s1.items.keys())
print(s1.items.get("bread"))
print("-" * 50)
s1.remove_item("cookies", 2)
s1.remove_item("bread", 12)
print(s1.items)
print(s1.get_total_cost())

print(list_out_of_stock_products())
