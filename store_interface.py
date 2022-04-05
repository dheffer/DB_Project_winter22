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


def submit_action():
    name = string_user_name.get()
    password = string_user_password.get()
    if password == 'greghard0001' and name == 'AA0001':
        string_message.set('Successful Login')
    else:
        string_message.set('Incorrect Login Credentials')

root = tk.Tk()
root.title('Generic Vehicle Merchant Software')
root.geometry('600x200')

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

ttk.Button(frame_home, text='submit', command=submit_action).grid(column=1, row=2, columnspan=2)

root.mainloop()