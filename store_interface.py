"""
This file is for creation of what the user will see
Our version of our own DBMS
"""
import tkinter as tk
from tkinter import ttk

# TODO: -area to enter username and password,
#  -area to place an order from a vendor
#  -add or remove product from cart
#  -invoice creation on sale
#  -area to input customer data (for new customer)

# create the root window
root = tk.Tk()
root.title("Generic Vehicle Merchant Software")
root.geometry("600x400")

# create the main frame
frame_home = ttk.Frame(root)
frame_home.pack(fill=tk.BOTH, expand=True)

root.mainloop()
