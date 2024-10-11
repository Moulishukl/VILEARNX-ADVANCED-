from tkinter import *
from tkinter import messagebox

# Inventory list to store products
inventory = []

# Function to add a product
def add_product():
    name = entry_name.get()
    quantity = entry_quantity.get()
    price = entry_price.get()
    
    if name and quantity.isdigit() and price.isdigit():
        inventory.append({'name': name, 'quantity': int(quantity), 'price': int(price)})
        messagebox.showinfo("Success", "Product added successfully!")
        entry_name.delete(0, END)
        entry_quantity.delete(0, END)
        entry_price.delete(0, END)
        show_inventory()
    else:
        messagebox.showerror("Error", "Please enter valid product details")

# Function to show the inventory
def show_inventory():
    listbox_products.delete(0, END)
    for product in inventory:
        listbox_products.insert(END, f"{product['name']} - Quantity: {product['quantity']}, Price: ${product['price']}")

# Creating the GUI window
root = Tk()
root.title("Simple Inventory Management System")
root.geometry("400x400")

# Product Name
Label(root, text="Product Name").pack()
entry_name = Entry(root)
entry_name.pack()

# Product Quantity
Label(root, text="Product Quantity").pack()
entry_quantity = Entry(root)
entry_quantity.pack()

# Product Price
Label(root, text="Product Price").pack()
entry_price = Entry(root)
entry_price.pack()

# Add Product Button
Button(root, text="Add Product", command=add_product).pack()

# Listbox to show inventory
Label(root, text="Inventory:").pack()
listbox_products = Listbox(root, width=50)
listbox_products.pack()

# Main loop to run the application
root.mainloop()