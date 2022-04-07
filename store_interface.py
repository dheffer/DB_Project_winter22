"""
This file is for creation of what the user will see
Our version of our own DBMS
"""

# TODO: -user sign in area
#   - add new customer details area
#   - button to list active users in past month
#   - shopping cart area, with add/remove features (track user id/name as well)
#   - area to order parts/vehicles from vendor
#   - button to list all products from store
#   - button to list everything out of stock
#   - finalize order button

# create the root window
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msgb
from store_backend import *

HOST = "localhost"
USER = "root"
PASS = "chimoCOCOsQl1202"  # DON'T SAVE YOUR PASSWORD TO GIT, MAKE SURE YOU REMOVE IT BEFORE PUSHING
DATABASE = "generic_vehicle_merchant"


def submit_action():
    name = string_user_name.get()
    password = string_user_password.get()
    if name == '1' and password == '123':
        string_message.set('Successful Login')
        shop_win()
    else:
        string_message.set('Incorrect Login Credentials')


def shop_win():
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

    """     
    Below: Adding Customer to Database
    """
    customer_info_frame = ttk.Frame(root2, width=80, height=100)
    customer_info_frame.pack(fill=tk.BOTH, expand=True)
    ttk.Label(customer_info_frame, text="Add Customer to Database").grid(column=1, row=0)

    ttk.Label(customer_info_frame, text="Customer Name: ").grid(column=0, row=1, sticky="w")
    cust_name = tk.StringVar()
    name_entry = ttk.Entry(customer_info_frame, width=40, textvariable=cust_name).grid(column=1, row=1)
    cust_name.set(name_entry)

    ttk.Label(customer_info_frame, text="Cust. Email: ").grid(column=0, row=2, sticky="w")
    cust_email = tk.StringVar()
    ttk.Entry(customer_info_frame, width=40, textvariable=cust_email).grid(column=1, row=2)

    ttk.Label(customer_info_frame, text="Cust. Address: ").grid(column=0, row=3, sticky="w")
    cust_address = tk.StringVar()

    ttk.Entry(customer_info_frame, width=40, textvariable=cust_address).grid(column=1, row=3)

    ttk.Label(customer_info_frame, text="Cust. Phone #: ").grid(column=0, row=4, sticky="w")
    cust_phone = tk.IntVar()
    ttk.Entry(customer_info_frame, width=40, textvariable=cust_phone).grid(column=1, row=4)

    ttk.Label(customer_info_frame, text="Cust. License #: ").grid(column=0, row=5, sticky="w")
    cust_license = tk.IntVar()
    ttk.Entry(customer_info_frame, width=40, textvariable=cust_license).grid(column=1, row=5)

    # TODO: FUCKING FIX THIS IM TIRED OF WORKING ON IT ITS BEEN 7 HOURS
    def customer_data_input_to_db():
        with connect(host=HOST, user=USER, password=PASS, database=DATABASE) as mysql_connection:
            with mysql_connection.cursor() as cursor:
                c_name = str(cust_name.get())
                c_email = str(cust_email.get())
                c_address = str(cust_address.get())
                c_phone = int(cust_phone.get())
                c_license = int(cust_license.get())
                cursor.execute(f"INSERT INTO generic_vehicle_merchant.customer (cust_name, "
                               f"cust_email, cust_address, cust_phone, cust_license) "
                               f"VALUES ('{c_name}', '{c_email}', '{c_address}', {c_phone}, {c_license})")
                print(f'{c_name}', f'{c_email}', f'{c_address}', {c_phone}, {c_license})
                mysql_connection.commit()
                msgb._show("Data Submitted", f"{cust_name} added to your database!")
                mysql_connection.close()

    ttk.Button(customer_info_frame,
               text="SUBMIT",
               command=customer_data_input_to_db).grid(column=1, row=6)

    """
    Out of Stock Functionality
    """
    ttk.Button(frame_home2, text='Out of Stock items', command=out_stock).grid(column=4,
                                                                               row=0,
                                                                               columnspan=2)

    root2.mainloop()


def out_stock():
    root3 = tk.Tk()
    root3.title('Out Of Stock')
    root3.geometry('200x100')
    frame_home3 = ttk.Frame(root3)
    frame_home3.pack(fill=tk.BOTH, expand=True)
    ttk.Label(frame_home3, text="Product 1").grid(column=0, row=0)
    ttk.Label(frame_home3, text="Product 2").grid(column=0, row=1)
    ttk.Label(frame_home3, text="Product 3").grid(column=0, row=2)
    ttk.Label(frame_home3, text="Product 4").grid(column=0, row=3)


root = tk.Tk()
root.title('GVM Login')
root.geometry('300x100')

frame_home = ttk.Frame(root)
frame_home.pack(fill=tk.BOTH, expand=True)

ttk.Label(frame_home, text="Name: ").grid(column=0, row=0)
ttk.Label(frame_home, text="Password: ").grid(column=0, row=1)

string_user_name = tk.StringVar()
ttk.Entry(frame_home, width=30, textvariable=string_user_name).grid(column=1, row=0)

string_user_password = tk.StringVar()
ttk.Entry(frame_home, width=30, textvariable=string_user_password).grid(column=1, row=1)

string_message = tk.StringVar()
ttk.Entry(frame_home, width=30, textvariable=string_message).grid(column=1, row=3, columnspan=2)

ttk.Button(frame_home, text='SUBMIT', command=submit_action).grid(column=1, row=2, columnspan=2)

root.mainloop()
