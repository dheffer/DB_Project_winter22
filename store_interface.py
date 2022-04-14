"""
This file is for creation of what the user will see
Our version of our own DBMS
"""

# create the root window
from mysql.connector import connect
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msgb
from details import *


user_login = False


# LOGIN GUI BELOW
def check_login_details():
    name = string_user_name.get()
    password = string_user_password.get()
    if name == log_name and password == log_pass:
        global user_login
        string_message.set('Successful Login')
        user_login = True
        login.destroy()
    else:
        string_message.set('Incorrect Login Credentials')


login = tk.Tk()
login.title('GVM Login Screen')
login.geometry('300x110')

frame_home = ttk.Frame(login)
frame_home.pack(fill=tk.BOTH, expand=True)

ttk.Label(frame_home, text="Name: ").grid(column=0, row=0)
ttk.Label(frame_home, text="Password: ").grid(column=0, row=1)

string_user_name = tk.StringVar()
ttk.Entry(frame_home, width=30, textvariable=string_user_name).grid(column=1, row=0)

string_user_password = tk.StringVar()
ttk.Entry(frame_home, width=30, textvariable=string_user_password).grid(column=1, row=1)

string_message = tk.StringVar()
ttk.Entry(frame_home, width=30, textvariable=string_message).grid(column=1, row=3, columnspan=2)

ttk.Button(frame_home, text='SUBMIT', command=check_login_details).grid(column=1, row=2, columnspan=2)
login.mainloop()


# LOGIN GUI ABOVE


def customer_submit():
    global user_login
    if user_login:
        with connect(host=HOST, user=USER, password=PASS, database=DATABASE) as mysql_connection:
            with mysql_connection.cursor() as cursor:
                cust_name = str(customer_name.get())
                cust_email = str(customer_email.get())
                cust_address = str(customer_address.get())
                cust_phone = int(str(customer_phone.get()))
                cust_license = int(str(customer_license.get()))
                query = ("INSERT INTO generic_vehicle_merchant.customer (cust_name, cust_email, cust_address, "
                         "cust_phone, cust_license) "
                         "VALUES (%s, %s, %s, %s, %s)")
                cust_info = (f"{cust_name}",
                             f"{cust_email}",
                             f"{cust_address}",
                             cust_phone,
                             cust_license)
                cursor.execute(query, cust_info)
                mysql_connection.commit()
                mysql_connection.close()
                return msgb.showinfo("Complete", "Customer added!")
    elif not user_login:
        return msgb.showwarning("ERROR!", "You must login to make changes!")


root = tk.Tk()
root.title('GVM Application')
root.geometry('900x500')

# ADD_CUSTOMER FIELDS BELOW
customer_name = tk.StringVar()
customer_email = tk.StringVar()
customer_address = tk.StringVar()
customer_phone = tk.StringVar()
customer_license = tk.StringVar()

root_frame = ttk.Frame(root)
root_frame.pack(fill=tk.BOTH, expand=True)
ttk.Label(root_frame,
          background="#D4FDF9",
          text="Add Customer to Database").grid(column=1,
                                                row=0)
ttk.Label(root_frame,
          background="#F9E3E5",
          text="Customer Name: ").grid(column=0, row=1, sticky="w")
ttk.Entry(root_frame,
          width=40,
          textvariable=customer_name).grid(column=1, row=1)
ttk.Label(root_frame,
          background="#F9E3E5",
          text="Cust. Email: ").grid(column=0, row=2, sticky="w")
ttk.Entry(root_frame,
          width=40,
          textvariable=customer_email).grid(column=1, row=2)
ttk.Label(root_frame,
          background="#F9E3E5",
          text="Cust. Address: ").grid(column=0, row=3, sticky="w")
ttk.Entry(root_frame,
          width=40,
          textvariable=customer_address).grid(column=1, row=3)
ttk.Label(root_frame,
          background="#F9E3E5",
          text="Cust. Phone #: ").grid(column=0, row=4, sticky="w")
ttk.Entry(root_frame,
          width=40,
          textvariable=customer_phone).grid(column=1, row=4)
ttk.Label(root_frame,
          background="#F9E3E5",
          text="Cust. License #: ").grid(column=0, row=5, sticky="w")
ttk.Entry(root_frame,
          width=40,
          textvariable=customer_license).grid(column=1, row=5)
ttk.Button(root_frame,
           text="SUBMIT CUSTOMER INFO",
           command=customer_submit).grid(column=1, row=6)


# ADD_CUSTOMER FIELDS ABOVE

# ACTIVE USERS IN THE LAST MONTH
def last_months_users():
    # Create connection
    with connect(host=HOST, user=USER, password=PASS) as mysql_connection_object:
        # Create cursor
        with mysql_connection_object.cursor() as mysql_cursor:
            # Create SQL statement
            update_statement = f"""USE generic_vehicle_merchant;"""
            update_statement2 = f"""SELECT customer.cust_name, invoice.time_of_sale
                                    from customer inner join invoice
                                    on customer.customer_id = invoice.customer_id
                                    where time_of_sale BETWEEN NOW() - INTERVAL 31 DAY AND NOW();"""
            # Execute the statement
            mysql_cursor.execute(update_statement)
            mysql_cursor.execute(update_statement2)
            user_list = ""
            count = 0
            for row in mysql_cursor:
                count += 1
                user_list += f"Customer: {str(row[0])}, Last Order: {str(row[1])}\n"
                # Commit the change
            mysql_connection_object.commit()
    users_textvar.set(f"{user_list}")


users_textvar = tk.StringVar()
users_textvar.set("")

ttk.Button(root_frame,
           text="SHOW ALL USERS IN THE LAST MONTH",
           command=last_months_users).grid(column=5,
                                           row=9,
                                           sticky=tk.W)
ttk.Label(root_frame, textvariable=users_textvar).grid(column=5,
                                                       row=10,
                                                       sticky=tk.W)


# OUT_OF_STOCK_PRODUCTS BELOW
def list_out_of_stock_products():
    """
    :return: returns a list of all out of stock products, useful to
     know when to order more
    """
    global user_login
    if user_login:
        with connect(host=HOST, user=USER, password=PASS) as mysql_connection:
            with mysql_connection.cursor() as mysql_cursor:
                query = f"""SELECT product_id, vehicle, cost, vendor_id, quantity
                  FROM generic_vehicle_merchant.products
                    WHERE quantity = {0}
                    """
                # CHANGE QUANTITY TO 10 OR WHATEVER VALUE TO TEST FUNCTIONALITY
                mysql_cursor.execute(query)
                out_of_stock = mysql_cursor.fetchall()
                no_items_list = ""
                count = 0
                for row in out_of_stock:
                    count += 1
                    no_items_list += f"Item: {str(row[1])}, Quantity: {row[4]}\n"

        no_item_textvar.set(f"{no_items_list}")
    elif not user_login:
        return msgb.showwarning("ERROR!", "You must login to make changes!")


no_item_textvar = tk.StringVar()
no_item_textvar.set("")
ttk.Button(root_frame,
           text="SHOW OUT OF STOCK ITEMS",
           command=list_out_of_stock_products).grid(column=1,
                                                    row=9)

ttk.Label(root_frame,
          textvariable=no_item_textvar,
          anchor=tk.S).grid(column=1,
                            row=10)

# OUT_OF_STOCK_PRODUCTS ABOVE


def get_all_products():
    # Create connection
    global user_login
    if user_login:
        with connect(host=HOST, user=USER, password=PASS) as mysql_connection_object:
            # Create cursor
            with mysql_connection_object.cursor() as mysql_cursor:
                # Create SQL statement
                update_statement = f"""USE generic_vehicle_merchant;"""
                update_statement2 = f"""SELECT vehicle
                                        FROM `generic_vehicle_merchant`.`products`;"""
                # Execute the statement
                mysql_cursor.execute(update_statement)
                mysql_cursor.execute(update_statement2)
                items_list = ""
                count = 0
                for row in mysql_cursor:
                    count += 1
                    items_list += f"Item: {str(row[0])}\n"
                # Commit the change
                mysql_connection_object.commit()
        all_item_textvar.set(f"{items_list}")
    elif not user_login:
        return msgb.showwarning("ERROR!", "You must login to make changes!")


all_item_textvar = tk.StringVar()
all_item_textvar.set("")

ttk.Button(root_frame,
           text="SHOW ALL PRODUCTS",
           command=get_all_products).grid(column=3,
                                          row=9)
ttk.Label(root_frame,
          textvariable=all_item_textvar).grid(column=3,
                                              row=10)


# Get_all_products above


def update_from_vendor():
    # Create connection
    with connect(host=HOST, user=USER, password=PASS) as mysql_connection_object:
        # Create cursor
        with mysql_connection_object.cursor() as mysql_cursor:
            product_name = str(product.get())
            total_quantity = int(str(quantity.get()))
            # Create SQL statement
            update_statement = f"""USE generic_vehicle_merchant;"""
            update_statement2 = f"""UPDATE products
                                    SET quantity = quantity + {total_quantity}
                                    WHERE product_name = '{product_name}';"""
            # Execute the statement
            mysql_cursor.execute(update_statement)
            mysql_cursor.execute(update_statement2)
            # Commit the change
            mysql_connection_object.commit()
            msgb.showinfo("Updated", "You've ordered more product."
                                     "\nProduct Name:  " + product_name)



update_quan_textvar = tk.StringVar()
update_quan_textvar.set("")

ttk.Button(root_frame,
           text="CLICK TO ORDER PRODUCTS FROM VENDOR",
           command=update_from_vendor).grid(column=1,
                                            row=12)
product = tk.StringVar()
quantity = tk.IntVar()
ttk.Entry(root_frame,
          width=40,
          textvariable=product).grid(column=1, row=13)
ttk.Label(root_frame,
          background="#F9E3E5",
          text="Product Name: ").grid(column=0, row=13, sticky="w")
ttk.Entry(root_frame,
          width=40,
          textvariable=quantity).grid(column=1, row=14)
ttk.Label(root_frame,
          background="#F9E3E5",
          text="Quantity: ").grid(column=0, row=14, sticky="w")
ttk.Label(root_frame,
          textvariable=update_quan_textvar,
          anchor=tk.S).grid(column=0,
                            row=12)

# SHOPPING_CART SECTION BELOW
cart_product_id = tk.StringVar()
cart_product_id.set("")

def add_to_cart():
    global total_value
    global cart_items
    global cart_display
    global user_login
    printed = False
    prod_id = int(cart_product_id.get())
    cart_quant = int(cart_quantity.get())
    if user_login:
        with connect(host=HOST, user=USER, password=PASS) as mysql_connection_object:
            # Create cursor
            with mysql_connection_object.cursor() as mysql_cursor:
                # Create SQL statement
                update_statement = f"""USE generic_vehicle_merchant;"""
                update_statement2 = f"""SELECT vehicle
                                        FROM `generic_vehicle_merchant`.`products`
                                        WHERE product_id = {prod_id};"""
                mysql_cursor.execute(update_statement)
                mysql_cursor.execute(update_statement2)
                name = mysql_cursor.fetchall()
                v_name = name[0]
                # Commit the change
                mysql_connection_object.commit()
    if v_name not in cart_items.keys():
        cart_items.update({v_name: cart_quant})
        print(f"1. {cart_items}")
    elif v_name in cart_items.keys():
        update = cart_items[v_name] + cart_quant
        cart_items.update({v_name: update})
        print(f"2. {cart_items}")
    else:
        return print(f"3. {cart_items}")

    key_value = ""
    for keys, values in cart_items.items():
        key = f"Product Name: {str(keys[0])}\t"
        value = f"Quantity: {values}\n"
        key_value += key + value
        total_value = value
    cart_display_stringvar.set(key_value)


def remove_from_cart():
    global cart_items
    global cart_display
    prod_id = int(cart_product_id.get())
    cart_quant = int(cart_quantity.get())
    if user_login:
        with connect(host=HOST, user=USER, password=PASS) as mysql_connection_object:
            # Create cursor
            with mysql_connection_object.cursor() as mysql_cursor:
                # Create SQL statement
                update_statement = f"""USE generic_vehicle_merchant;"""
                update_statement2 = f"""SELECT vehicle
                                        FROM `generic_vehicle_merchant`.`products`
                                        WHERE product_id = {prod_id};"""
                mysql_cursor.execute(update_statement)
                mysql_cursor.execute(update_statement2)
                name = mysql_cursor.fetchall()
                v_name = name[0]
    if v_name not in cart_items.keys():
        msgb.showwarning("ERROR", "The item isn't in your cart!")
        raise AssertionError("This item isn't in your shopping cart")

    # deletes item from shopping cart if quantity specified is greater than amount in cart
    elif cart_items[v_name] <= cart_quant:
        cart_items.pop(v_name)
        print(f"4. {cart_items}")

    # if quantity specified is less than cart amount, subtract that amount from cart
    elif cart_items[v_name] > cart_quant:
        modified = cart_items[v_name] - cart_quant
        cart_items.update({v_name: modified})
        print(f"5. {cart_items}")

    key_value = ""
    for keys, values in cart_items.items():
        key = f"Product Name: {str(keys[0])}\t"
        value = f"Quantity: {values}\n"
        key_value += key + value
    cart_display_stringvar.set(key_value)


def get_cust_id():
    global cust_id
    # Create connection
    customer_name = cart_customer.get()
    with connect(host=HOST, user=USER, password=PASS) as mysql_connection_object:
        # Create cursor
        with mysql_connection_object.cursor() as mysql_cursor:
            # Create SQL statement
            update_statement = f"""USE generic_vehicle_merchant;"""
            update_statement2 = f"""select customer_id from customer
                                    where cust_name = "{customer_name}";"""
            # Execute the statement
            mysql_cursor.execute(update_statement)
            mysql_cursor.execute(update_statement2)
            cust_id = 0
            for ids in mysql_cursor:
                row_id = ids[0]
                cust_id = int(row_id)
            # Commit the change
            msgb.showinfo("Confirmed", "Customer ID: " + str(cust_id))
            return cust_id


def fill_orders():
    get_cust_id()
    global cust_id
    ids = cust_id
    # Create connection
    with connect(host=HOST, user=USER, password=PASS) as mysql_connection_object:
        # Create cursor
        with mysql_connection_object.cursor() as mysql_cursors:
            update_statement = f"""USE generic_vehicle_merchant;"""
            update_statement2 = f"""insert into orders(time_of_sale, customer_id)
                                    values (CURRENT_DATE(), {ids});"""
            # Execute the statement
            mysql_cursors.execute(update_statement)
            mysql_cursors.execute(update_statement2)
            # Commit the change
            mysql_connection_object.commit()
            msgb.showinfo("Order Filled", "Your order has been processed."
                                          "\nClick below to create an invoice!")
    fill_order_details()


def fill_order_details():
    prod = cart_product_id.get()
    quant = cart_quantity.get()
    # Create connection
    with connect(host=HOST, user=USER, password=PASS) as mysql_connection_object:
        # Create cursor
        with mysql_connection_object.cursor() as mysql_cursors:
            update_statement = f"""USE generic_vehicle_merchant;"""
            update_statement2 = f"""insert into order_details (order_id, product_id, quantity)
                                    values({recent_order_id()}, {prod}, {quant});"""
            # Execute the statement
            mysql_cursors.execute(update_statement)
            mysql_cursors.execute(update_statement2)
            # Commit the change
            mysql_connection_object.commit()


def recent_order_id():
    with connect(host=HOST, user=USER, password=PASS) as mysql_connection_object:
        with mysql_connection_object.cursor() as mysql_cursor:
            id_query = f"""select max(order_id) from generic_vehicle_merchant.orders
                            limit 1;"""
            mysql_cursor.execute(id_query)
            id_value = mysql_cursor.fetchall()
            recent_id_value = int(id_value[0][0])
            return recent_id_value


# ALL FUNCTIONS FOR FINALIZING INVOICE
def get_invoice():
    global cust_id
    # Create connection
    with connect(host=HOST, user=USER, password=PASS) as mysql_connection_object:
        # Create cursor
        with mysql_connection_object.cursor() as mysql_cursors:
            update_statement = f"""USE generic_vehicle_merchant;"""
            update_statement2 = f"""insert into invoice (order_id, time_of_sale, customer_id)
                                    values({recent_order_id()}, CURRENT_DATE(), {cust_id});"""
            # Execute the statement
            mysql_cursors.execute(update_statement)
            mysql_cursors.execute(update_statement2)
            # Commit the change
            mysql_connection_object.commit()


def invoice_details():
    invoice_quantity_remove()
    get_invoice()
    with connect(host=HOST, user=USER, password=PASS) as mysql_connection_object:
        # Create cursor
        with mysql_connection_object.cursor() as mysql_cursor:
            o_id = recent_order_id()
            # Create SQL statement
            update_statement = f"""USE generic_vehicle_merchant;"""
            update_statement2 = f"""select invoice.invoice_id, invoice.time_of_sale, invoice.customer_id, order_details.product_id, order_details.quantity
                                        from invoice inner join order_details
                                        on invoice.order_id = order_details.order_id
                                        where order_details.order_id = {o_id};"""
            # Execute the statement
            mysql_cursor.execute(update_statement)
            mysql_cursor.execute(update_statement2)
            details = mysql_cursor.fetchall()
            o_details = details
            inv_id = []
            tos = []
            c_id = []
            for i in o_details:
                inv_id.append(i[0])
                tos.append(i[1])
                c_id.append(i[2])
            update_statement4 = f"select cust_name from customer where customer_id = {c_id[0]}"
            mysql_cursor.execute(update_statement4)
            customer_name = mysql_cursor.fetchall()
            name = f"Name: {customer_name[0][0]}"
            cart_list = []
            cart_values = []
            for row in cart_items.keys():
                cart_list.append(row[0])
            for row in cart_items.values():
                cart_values.append(row)
            mysql_connection_object.commit()
            msgb.showinfo("Invoice",
                          f"\nInvoice Number: {inv_id[0]}\t"
                          f"\nDate: {tos[0]}\t"
                          f"\n{name}\t"
                          f"\nProduct Name: {cart_list}\t"
                          f"\nQuantity: {cart_values}")
            inv_id.clear()
            tos.clear()
            c_id.clear()
            # Commit the change


def invoice_quantity_remove():
    # Create connection
    with connect(host=HOST, user=USER, password=PASS) as mysql_connection_object:
        # Create cursor
        with mysql_connection_object.cursor() as mysql_cursor:
            prod = cart_product_id.get()
            quant = cart_quantity.get()
            # Create SQL statement
            update_statement = f"""USE generic_vehicle_merchant;"""
            update_statement2 = f"""UPDATE products
                                    SET quantity = quantity - {quant}
                                    WHERE product_id = '{prod}';"""
            # Execute the statement
            mysql_cursor.execute(update_statement)
            mysql_cursor.execute(update_statement2)
            # Commit the change
            mysql_connection_object.commit()


ttk.Button(root_frame,
           text="GENERATE"
                "\nINVOICE",
           command=invoice_details).grid(column=4, row=13)

cust_id = 0
total_value = 0
# ADD TO CART
cart_items = {}
cart_item_stringvar = tk.StringVar()
cart_item_stringvar.set(cart_items)

cart_display_stringvar = tk.StringVar()
cart_display = ""

ttk.Label(root_frame,
          background="#D4FDF9",
          text="Shopping Cart").grid(column=4, row=0)
cart_product_id = tk.IntVar()
cart_quantity = tk.IntVar()
ttk.Label(root_frame,
          background="#F9E3E5",
          text="Product ID: ").grid(column=3, row=1)
ttk.Entry(root_frame,
          width=15,
          textvariable=cart_product_id).grid(column=4, row=1)

ttk.Label(root_frame,
          background="#F9E3E5",
          text="Customer: ").grid(column=3, row=3)
cart_customer = tk.StringVar()
ttk.Entry(root_frame,
          width=15,
          textvariable=cart_customer).grid(column=4, row=3)

ttk.Label(root_frame,
          background="#F9E3E5",
          text="Quantity: ").grid(column=3, row=2)
ttk.Entry(root_frame,
          width=15,
          textvariable=cart_quantity).grid(column=4, row=2)
ttk.Button(root_frame,
           text="+",
           command=add_to_cart,
           width=5).grid(column=4, row=4, sticky=tk.W)
ttk.Button(root_frame,
           text="-",
           command=remove_from_cart,
           width=5).grid(column=4, row=4, sticky=tk.E)

ttk.Button(root_frame,
           text="CONFIRM NAME",
           command=get_cust_id,
           width=20).grid(column=3, row=5, columnspan=2, sticky=tk.E)

# CART COMPLETE ORDER
ttk.Button(root_frame,
           text="COMPLETE ORDER",
           command=fill_orders,
           width=18).grid(column=5, row=6, columnspan=2)

# CART ITEMS LIST
ttk.Label(root_frame,
          background="#D4FDF9",
          text="Cart Items").grid(column=5, row=0)
ttk.Label(root_frame,
          textvariable=cart_display_stringvar).grid(column=5, row=1)

root.mainloop()
