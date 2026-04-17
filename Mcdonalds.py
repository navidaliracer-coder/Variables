import tkinter as tk
from tkinter import ttk, messagebox

class RestaurantOrderManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("McDonalds Mangament =)")

        self.menu_items = {
            "Small Fries" : 2,
            "Lunch Combo" : 2,
            "Big Mac" : 3,
            "Happy Meal" : 4,
            "Cheeseburger" : 2.5,
            "Coke" : 1
        }

        self.exchange_rate = 82

        self.setup_backround(root)

        frame = ttk.Frame(root)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        ttk.Label(
            frame,
            text="Mcdonalds Mangament =)",
            font=("Arial", "20", "bold"),
        ).grid(row=0, columnspan = 3, padx =10, pady=10)

        self.menu_labels = {}
        self.menu_quantities = {}

        for i, (item, price) in enumerate(self.menu.items.items(), start=1):
            label = ttk.Label(
                frame,
                text= f {item} (${price}):",
                font = ("Arial", 12),
            )
            label.grid(row=i, column=0, padx=10, pady=5)
            self.menu_labels[item] = label
            
            quantity_entry = ttk.Entry(frame, width=5)
            self.menu_labels[items] = label
            quantity_entry.grid(row=i, column, padx=10, pady=5)
            self.menu_labels[item] = label

        self.currency_var = tk.StringVar()
        ttk.label(
            frame, 
            text="Currency:",
            font=("Arial", 12)
        ).grid(
            row=len(self.menu_items) + 1,
            column=0,
            padx=10,
            pady=5,
        )

        currency_dropdown = ttk.Combobox(
            frame,
            textvariable=self, currency=var,
            state="readonly",
            width=18
            values=("CAD")
        )
        currency_dropdown.current(0)
        self.currency_var.trace("w", self.update_menu_prices)

        order_button = ttk.Button(
            frame,



        


            
        
