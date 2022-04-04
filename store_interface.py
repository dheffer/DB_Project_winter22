"""
This file is for creation of what the user will see
Our version of our own DBMS
"""
import tkinter as tk
from tkinter import ttk

# TODO: -user sign in area
#   - add new customer details area
#   - button to list active users in past month
#   - shopping cart area, with add/remove features (track user id/name as well)
#   - area to order parts/vehicles from vendor
#   - button to list all products from store
#   - button to list everything out of stock
#   - finalize order button

# create the root window
root = tk.Tk()
root.title("Generic Vehicle Merchant Software")
root.geometry("600x400")

# create the main frame
frame_home = ttk.Frame(root)
frame_home.pack(fill=tk.BOTH, expand=True)

root.mainloop()
