"""
This file is for creation of what the user will see
Our version of our own DBMS
"""

# TODO: button to list active users in past month
# TODO: shopping cart area, with add/remove features (track user id/name as well)
# TODO: area to order parts/vehicles from vendor
# TODO: button to list all products from store DONE
# TODO: button to list everything out of stock DONE
# TODO: finalize order button

# create the root window
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msgb
from store_backend import *

user_login = False


# LOGIN GUI BELOW
def check_login_details():
    name = string_user_name.get()
    password = string_user_password.get()
    if name == '1' and password == '123':
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
root.geometry('800x800')

# ADD_CUSTOMER FIELDS BELOW
customer_name = tk.StringVar()
customer_email = tk.StringVar()
customer_address = tk.StringVar()
customer_phone = tk.StringVar()
customer_license = tk.StringVar()

customer_info_frame = ttk.Frame(root)
customer_info_frame.pack(fill=tk.BOTH, expand=True)
ttk.Label(customer_info_frame,
          background="#D4FDF9",
          text="Add Customer to Database").grid(column=1,
                                                row=0)
ttk.Label(customer_info_frame,
          background="#F9E3E5",
          text="Customer Name: ").grid(column=0, row=1, sticky="w")
ttk.Entry(customer_info_frame,
          width=40,
          textvariable=customer_name).grid(column=1, row=1)
ttk.Label(customer_info_frame,
          background="#F9E3E5",
          text="Cust. Email: ").grid(column=0, row=2, sticky="w")
ttk.Entry(customer_info_frame,
          width=40,
          textvariable=customer_email).grid(column=1, row=2)
ttk.Label(customer_info_frame,
          background="#F9E3E5",
          text="Cust. Address: ").grid(column=0, row=3, sticky="w")
ttk.Entry(customer_info_frame,
          width=40,
          textvariable=customer_address).grid(column=1, row=3)
ttk.Label(customer_info_frame,
          background="#F9E3E5",
          text="Cust. Phone #: ").grid(column=0, row=4, sticky="w")
ttk.Entry(customer_info_frame,
          width=40,
          textvariable=customer_phone).grid(column=1, row=4)
ttk.Label(customer_info_frame,
          background="#F9E3E5",
          text="Cust. License #: ").grid(column=0, row=5, sticky="w")
ttk.Entry(customer_info_frame,
          width=40,
          textvariable=customer_license).grid(column=1, row=5)
ttk.Button(customer_info_frame,
           text="SUBMIT",
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
last_month_frame = ttk.Frame(root)
last_month_frame.pack(fill=tk.BOTH, expand=True)
ttk.Button(last_month_frame,text="CLICK TO SHOW ALL USERS IN THE LAST MONTH",command=last_months_users).grid(column=3,row=2)
ttk.Label(last_month_frame, textvariable=users_textvar,anchor=tk.N).grid(column=3,row=3)

# OUT_OF_STOCK_PRODUCTS BELOW
def list_out_of_stock_products():
    """
    :return: returns a list of all out of stock products, useful to
     know when to order more
    """
    # TODO: incorporate with GUI
    global user_login
    if user_login:
        with connect(host=HOST, user=USER, password=PASS) as mysql_connection:
            with mysql_connection.cursor() as mysql_cursor:
                query = f"""SELECT product_id, vehicle, cost, vendor_id, quantity
                  FROM generic_vehicle_merchant.products
                    WHERE quantity = {10}
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
no_stock_frame = ttk.Frame(root)
no_stock_frame.pack(fill=tk.BOTH, expand=True)
ttk.Button(no_stock_frame,
           text="CLICK TO SHOW OUT OF STOCK ITEMS",
           command=list_out_of_stock_products).grid(column=1,
                                                    row=5)

ttk.Label(no_stock_frame,
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
all_stock_frame = ttk.Frame(root)
all_stock_frame.pack(fill=tk.BOTH, expand=True)
ttk.Button(all_stock_frame,
           text="CLICK TO SHOW ALL PRODUCTS",
           command=get_all_products).grid(column=2,
                                                    row=5)
ttk.Label(all_stock_frame,
          textvariable=all_item_textvar,
          anchor=tk.S).grid(column=2,
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
                                    SET quantity = {total_quantity}
                                    WHERE product_name = '{product_name}';"""
            # Execute the statement
            mysql_cursor.execute(update_statement)
            mysql_cursor.execute(update_statement2)
            # Commit the change
            mysql_connection_object.commit()

update_quan_textvar = tk.StringVar()
update_quan_textvar.set("")
update_quan_frame = ttk.Frame(root)
update_quan_frame.pack(fill=tk.BOTH, expand=True)
ttk.Button(update_quan_frame,
           text="ORDER PRODUCTS FROM VENDOR HERE!",
           command=update_from_vendor).grid(column=1,
                                                    row=12)
product = tk.StringVar()
quantity = tk.IntVar()
ttk.Entry(update_quan_frame,
          width=40,
          textvariable=product).grid(column=1, row=13)
ttk.Label(update_quan_frame,
          background="#F9E3E5",
          text="Product Name: ").grid(column=0, row=13, sticky="w")
ttk.Entry(update_quan_frame,
          width=40,
          textvariable=quantity).grid(column=1, row=14)
ttk.Label(customer_info_frame,
          background="#F9E3E5",
          text="Quantity: ").grid(column=0, row=14, sticky="w")
ttk.Label(update_quan_frame,
          textvariable=update_quan_textvar,
          anchor=tk.S).grid(column=0,
                            row=12)


# GET_FROM_VENDOR(if the quantity is less than what customer orders get parts from vendor)
root.mainloop()


def shop_win():
    # TODO: this needs to be resorted because it's currently non-functional
    root2 = tk.Tk()
    root2.title('Generic Vehicle Merchant Software')
    root2.geometry('800x600')
    frame_home2 = ttk.Frame(root2)
    frame_home2.pack(fill=tk.BOTH, expand=True)
    ttk.Label(frame_home2, text="Product 1").grid(column=0, row=0)
    ttk.Label(frame_home2, text="Product 2").grid(column=1, row=0)
    ttk.Label(frame_home2, text="Product 3").grid(column=2, row=0)
    ttk.Label(frame_home2, text="Product 4").grid(column=3, row=0)
    ttk.Button(frame_home2, text='+').grid(column=0, row=1, columnspan=1)
    ttk.Button(frame_home2, text='-').grid(column=0, row=2, columnspan=1)
    ttk.Button(frame_home2, text='+').grid(column=1, row=1, columnspan=1)
    ttk.Button(frame_home2, text='-').grid(column=1, row=2, columnspan=1)
    ttk.Button(frame_home2, text='+').grid(column=2, row=1, columnspan=1)
    ttk.Button(frame_home2, text='-').grid(column=2, row=2, columnspan=1)
    ttk.Button(frame_home2, text='+').grid(column=3, row=1, columnspan=1)
    ttk.Button(frame_home2, text='-').grid(column=3, row=2, columnspan=1)

    ttk.Button(frame_home2, text='Out of Stock items', command=out_stock).grid(column=4,
                                                                               row=0,
                                                                               columnspan=2)

    root2.mainloop()


def out_stock():
    # TODO: this also needs to be resorted
    root3 = tk.Tk()
    root3.title('Out Of Stock')
    root3.geometry('200x100')
    frame_home3 = ttk.Frame(root3)
    frame_home3.pack(fill=tk.BOTH, expand=True)
    ttk.Label(frame_home3, text="Product 1").grid(column=0, row=0)
    ttk.Label(frame_home3, text="Product 2").grid(column=0, row=1)
    ttk.Label(frame_home3, text="Product 3").grid(column=0, row=2)
    ttk.Label(frame_home3, text="Product 4").grid(column=0, row=3)
