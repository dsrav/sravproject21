import tkinter as tk
import pandas as pd
import qrcode
import sqlite3
from tkinter import *


# Connect to the database
conn = sqlite3.connect("Fashion Resolutions.db")
cursor = conn.cursor()


# Create the login window
def login():
  window = tk.Tk()
  window.title("Fashion Resolutions")
  # Open the login window
  login_window = tk.Toplevel(window)
  login_window.title("Login")
  # Add a label for the email
  tk.Label(login_window, text="Email:").pack()
  # Add an entry field for the email
  email_entry = tk.Entry(login_window)
  email_entry.pack()
  # Add a label for the password
  tk.Label(login_window, text="Password:").pack()
  # Add an entry field for the password
  password_entry = tk.Entry(login_window, show="*")
  password_entry.pack()
  password_entry.mainloop()
login()

# Check the login credentials
def check_login(email, password):
  # Query the database to find the user
  cursor.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
  user = cursor.fetchone()
  if user:
    # If the login is successful, open the user menu
    user_menu()
  else:
    # If the login is unsuccessful, display an error message
    error_label.config(text="Invalid email or password")
check_login()

# User menu
def user_menu():
  # Open the user menu window
  user_menu_window = tk.Toplevel(window)
  user_menu_window.title("User Menu")
  # Add a button to select an item
  tk.Button(user_menu_window, text="Select Item", command=lambda: select_item()).pack()
  # Add a button to view the quantity of a specific item
  tk.Button(user_menu_window, text="View Item Quantity", command=lambda: view_item_quantity()).pack()
  # Add a button to view the entire inventory
  tk.Button(user_menu_window, text="View Inventory", command=lambda: view_inventory()).pack()
  # Add a button to retrieve an old transaction
  tk.Button(user_menu_window, text="Retrieve Transaction", command=lambda: retrieve_transaction()).pack()
  # Add a button to return a purchased item
  tk.Button(user_menu_window,text="Return Purchased Item", command=lambda: return_purchased_item()).pack()
  #Adding button for item returned to be added to the inventory
  tk.Button(user_menu_window, text="Returned item added to the inventory", command=lambda: return_item()).pack()
user_menu()

item_list = {
    "item1": {"code": "001", "name": "shirt", "price": "$9.00"},
    "item2": {"code": "002", "name": "jeans", "price": "$10.50"},
    "item3": {"code": "003", "name": "hat", "price": "$1.50"}
}

selected_item = None

while selected_item == None:
    user_input = input("Enter item code or item name: ")
    for item in item_list:
        if user_input == item_list[item]["code"] or user_input == item_list[item]["name"]:
            selected_item = item_list[item]
            break
    if selected_item == None:
        print("Invalid item code or name. Please try again.")

print("You have selected: " + selected_item["name"] + ", with a price of " + selected_item["price"])

df = pd.DataFrame(
    [['shirt','617767','katie123@exampl.com','24','Pweosnsijd223'],
     ['jeans','656787','price123@example.com','45','Eifibuhj267'],
     ['hat','575778','kacey123@example.com','23','isbisbiB34']],
    columns=['name','code','email','password','quantity','password'])

df.info()

  # Select an item
def select_item():
    # Open the select item window
    select_item_window = tk.Toplevel(window)
    select_item_window.title("Select Item")
    # Add a label for the item code or name
    tk.Label(select_item_window, text="Enter the item code or name:").pack()
    # Add an entry field for the item code or name
    item_entry = tk.Entry(select_item_window)
    item_entry.pack()
    # Add a button to confirm the selection
    tk.Button(select_item_window, text="Confirm", command=lambda: confirm_selection(item_entry.get())).pack()
select_item()

  # Confirm the selection
def confirm_selection(item):
    # Check if the item is a code or a name
    if item.isdigit():
      # If the item is a code, query the database to get the item information
      cursor.execute("SELECT * FROM items WHERE code=?", (item,))
    else:
      # If the item is a name, query the database to get the item information
      cursor.execute("SELECT * FROM items WHERE name=?", (item,))
    item = cursor.fetchone()
    if item:
      # If the item exists, open the purchase window
      purchase_window(item)
    else:
      # If the item does not exist, display an error message
      error_label.config(text="Item not found")
confirm_selection()

  # Purchase window
def purchase_window(item):
    # Open the purchase window
    purchase_window = tk.Toplevel(window)
    purchase_window.title("Purchase")
    # Display the item information
    tk.Label(purchase_window, text=f"Code: {item[0]}").pack()
    tk.Label(purchase_window, text=f"Name: {item[1]}").pack()
    tk.Label(purchase_window, text=f"Price: {item[2]}").pack()
    tk.Label(purchase_window, text=f"Brand: {item[3]}").pack()
purchase_window()

    # View the quantity of a specific item
def view_item_quantity():
      # Open the view item quantity window
      view_item_quantity_window = tk.Toplevel(window)
      view_item_quantity_window.title("View Item Quantity")
      # Add a label for the item code or name
      tk.Label(view_item_quantity_window, text="Enter the item code or name:").pack()
      # Add an entry field for the item code or name
      item_entry = tk.Entry(view_item_quantity_window)
      item_entry.pack()
      # Add a button to confirm the selection
      tk.Button(view_item_quantity_window, text="Confirm",
                command=lambda: confirm_view_item_quantity(item_entry.get())).pack()
view_item_quantity()

    # View the entire inventory
def view_inventory():
      # Opening the view inventory window
      view_inventory_window = tk.Toplevel(window)
      view_inventory_window.title("View Inventory")
      #Adding a label for the item code or name
      tk.Label(view_inventory_window,text="View inventory:").pack()
      #Adding an entry field for the item code or name
      item_entry=tk.Entry(view_inventory_window)
      item_entry.pack()
      #Adding a button to view the selected item
      tk.Button(view_inventory_item_quantity(item_view.get())).pack()
view_inventory()

      #Confirming the to view the item quantity
def confirm_view_inventory_item_quantity(item):
       #Checking if the item is a code or a name
       if item.isdigit():
          # If the item is a code, query the database to get the item information
        cursor.execute("SELECT*FROM items WHERE code=?",(item))
       else:
          # If the item is a name, query the database to get the item information
        cursor.execute("SELECT * FROM items WHERE name=?", (item,))
        item = cursor.fetchone()
       if item:
          #If item exists, display the item quantity
          tk.Label(view_item_inventory_quantity_window,text=f"Quantity:{item[3]}").pack()
       else:
           #If the item does not exist, display an error message
           error_label.config(text="Item not found")
confirm_view_inventory_item_quantity()

# Retrieve an old transaction
def retrieve_transaction():
  # Open the retrieve transaction window
  retrieve_transaction_window = tk.Toplevel(window)
  retrieve_transaction_window.title("Retrieve Transaction")
  # Add a label for the receipt number or QR code
  tk.Label(retrieve_transaction_window, text="Enter the receipt number or scan the QR code:").pack()
  # Add an entry field for the receipt number or QR code
  receipt_entry = tk.Entry(retrieve_transaction_window)
  receipt_entry.pack()
  # Add a button to confirm the selection
  tk.Button(retrieve_transaction_window, text="Confirm", command=lambda: confirm_retrieve_transaction(receipt_entry.get())).pack()
retrieve_transaction()

# Confirm the selection to retrieve the transaction
def confirm_retrieve_transaction(receipt):
  # Check if the receipt is a number or a QR code
  if receipt.isdigit():
    # If the receipt is a number, query the database to get the transaction information
    cursor.execute("SELECT * FROM transactions WHERE receipt_number=?", (receipt,))
  else:
    # If the receipt is a QR code, decode the QR code and get the receipt number
    receipt_number = qrcode.decode(receipt)
    # Query the database to get the transaction information
    cursor.execute("SELECT * FROM transactions WHERE receipt_number=?", (reciept,))
confirm_retrieve_transaction()

# Return an item
def return_item():
  # Open the return item window
  return_item_window = tk.Toplevel(window)
  return_item_window.title("Return Item")
  # Add a label for the receipt number or QR code
  tk.Label(return_item_window, text="Enter the receipt number or scan the QR code:").pack()
  # Add an entry field for the receipt number or QR code
  receipt_entry = tk.Entry(return_item_window)
  receipt_entry.pack()
  # Add a button to confirm the selection
  tk.Button(return_item_window, text="Confirm", command=lambda: confirm_return_item(receipt_entry.get())).pack()
return_item()

# Confirm the return of the item
def confirm_return_item(receipt):
  # Check if the receipt is a number or a QR code
  if receipt.isdigit():
    # If the receipt is a number, query the database to get the transaction information
    cursor.execute("SELECT * FROM transactions WHERE receipt_number=?", (receipt,))
  else:
    # If the receipt is a QR code, decode the QR code and get the receipt number
    receipt_number = qrcode.decode(receipt)
    # Query the database to get the transaction information
    cursor.execute("SELECT * FROM transactions WHERE receipt_number=?", (receipt_number,))
  transaction = cursor.fetchone()
  if transaction:
    # If the transaction exists, add the item back to the inventory
    cursor.execute("UPDATE items SET quantity=quantity+1 WHERE code=?", (transaction[1],))
    # Generate a return receipt
    generate_receipt(receipt_number, "return")
  else:
    # If the transaction does not exist, display an error message
    error_label.config(text="Transaction not found")
confirm_return_item()

# Generate a receipt
def generate_receipt(receipt_number, receipt_type):
  # Create a QR code for the receipt
  qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
  )
  qr.add_data(receipt_number)
  qr.make(fit=True)
  # Save the QR code image to a file
  image = qr.make_image(fill_color="black", back_color="white")
  image.save(f"receipt_{receipt_number}.png")
  # Print the receipt
  printer = Printer()
  printer.text(f"receipt_{receipt_number}.png")
generate_receipt()

# Add an item
def add_item():
    # Open the add item window
    add_item_window = tk.Toplevel(window)
    add_item_window.title("Add Item")
    # Add a label for the item code
    tk.Label(add_item_window, text="Enter the item code:").pack()
    # Add an entry field for the item code
    code_entry = tk.Entry(add_item_window)
    code_entry.pack()
    # Add a label for the item name
    tk.Label(add_item_window, text="Enter the item name:").pack()
    # Add an entry field for the item name
    name_entry = tk.Entry(add_item_window)
    name_entry.pack()
    # Add a label for the item quantity
    tk.Label(add_item_window, text="Enter the item quantity:").pack()
    # Add an entry field for the item quantity
    quantity_entry = tk.Entry(add_item_window)
    quantity_entry.pack()
    # Add a button to confirm the addition
    tk.Button(add_item_window, text="Confirm",
              command=lambda: confirm_add_item(code_entry.get(), name_entry.get(), quantity_entry.get())).pack()
add_item()

# Confirm the addition of the item
def confirm_add_item(code, name, quantity):
    # Check if the item code is not already in use
    cursor.execute("SELECT * FROM items WHERE code=?", (code,))
    item = cursor.fetchone()
    if item:
      # If the item code is already in use, display an error message
      error_label.config(text="Item code already in use")
    else:
      # If the item code is not already in use, add the item to the database
      cursor.execute("INSERT INTO items (code, name, quantity) VALUES (?, ?, ?)", (code, name, quantity))
      # Display a success message
      success_label.config(text="Item added successfully")
confirm_add_item()

      # Edit an item
def edit_item():
        # Open the edit item window
        edit_item_window = tk.Toplevel(window)
        edit_item_window.title("Edit Item")
        # Add a label for the item code
        tk.Label(edit_item_window, text="Enter the item code:").pack()
        # Add an entry field for the item code
        code_entry = tk.Entry(edit_item_window)
        code_entry.pack()
        # Add a label for the item name
        tk.Label(edit_item_window, text="Enter the item name:").pack()
        # Add an entry field for the item name
        name_entry = tk.Entry(edit_item_window)
        name_entry.pack()
        # Add a label for the item quantity
        tk.Label(edit_item_window, text="Enter the item quantity:").pack()
        # Add an entry field for the item quantity
        quantity_entry = tk.Entry(edit_item_window)
        quantity_entry.pack()
        # Add a button to confirm the edition
        tk.Button(edit_item_window, text="Confirm",
                  command=lambda: confirm_edit_item(code_entry.get(), name_entry.get(), quantity_entry.get())).pack()
edit_item()

      # Confirm the edition of the item
def confirm_edit_item(code, name, quantity):
        # Check if the item code exists
        cursor.execute("SELECT * FROM items WHERE code=?", (code,))
        item = cursor.fetchone()
        if item:
          # If the item code exists, update the item in the database
          cursor.execute("UPDATE items SET name=?, quantity=? WHERE code=?", (name, quantity, code))
          # Display a success message
          success_label.config(text="Item edited successfully")
        else:
          # If the item code does not exist, display an error message
          error_label.config(text="Item code does not exist")
confirm_edit_item()

        # Remove an item
def remove_item():
          # Open the remove item window
          remove_item_window = tk.Toplevel(window)
          remove_item_window.title("Remove Item")
          # Add a label for the item code
          tk.Label(remove_item_window, text="Enter the item code:").pack()
          # Add an entry field for the item code
          code_entry = tk.Entry(remove_item_window)
          code_entry.pack()
          # Add a button to confirm the removal
          tk.Button(remove_item_window, text="Confirm", command=lambda: confirm_remove_item(code_entry.get())).pack()
remove_item()

        # Confirm the removal of the item
def confirm_remove_item(code):
          # Check if the item code exists
          cursor.execute("SELECT * FROM items WHERE code=?", (code,))
          item = cursor.fetchone()
          if item:
            # If the item code exists, remove the item from the database
            cursor.execute("DELETE FROM items WHERE code=?", (code,))
            # Display a success message
            success_label.config(text="Item removed successfully")
          else:
            # If the item code does not exist, display an error message
            error_label.config(text="Item code does not exist")
confirm_remove_item()

            # Make an invoice
def make_invoice():
            # Open the make invoice window
            make_invoice_window = tk.Toplevel(window)
            make_invoice_window.title("Make Invoice")
            # Add a label for the item code
            tk.Label(make_invoice_window, text="Enter the item code:").pack()
            # Add an entry field for the item code
            code_entry = tk.Entry(make_invoice_window)
            code_entry.pack()
            # Add a label for the item quantity
            tk.Label(make_invoice_window, text="Enter the item quantity:").pack()
            # Add an entry field for the item quantity
            quantity_entry = tk.Entry(make_invoice_window)
            quantity_entry.pack()
            # Add a button to confirm the invoice
            tk.Button(make_invoice_window, text="Confirm",
                      command=lambda: confirm_make_invoice(code_entry.get(), quantity_entry.get())).pack()
make_invoice()

# Confirm the invoice
def confirm_make_invoice(code, quantity):
              # Check if the item code exists
              cursor.execute("SELECT * FROM items WHERE code=?", (code,))
              item = cursor.fetchone()
              for x in cursor:
                  print(x)
              if item:
                # If the item code exists, check if there is enough quantity
                if item[2] >= int(quantity):
                  # If there is enough quantity, decrease the quantity in the database
                  cursor.execute("UPDATE items SET quantity=? WHERE code=?",(item[2] - int(quantity), code))
                  # Generate a random reference number
                  reference_number = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
                  # Save the invoice in the database
                  cursor.execute("INSERT INTO invoices (reference_number, code, quantity) VALUES (?, ?, ?)",
                                 (reference_number, code, quantity))
                  # Generate the QR code for the invoice
                  img = qrcode.make(reference_number)
                  # Save the QR code in the local directory
                  img.save(reference_number + ".png")
                  # Display a success message
                success_label.config(text="Invoice made successfully")
              else:
                  # If there is not enough quantity, display an error message
                  error_label.config(text="Not enough quantity")
confirm_make_invoice()

              # Return an item
def return_item():
                # Open the return item window
                return_item_window = tk.Toplevel(window)
                return_item_window.title("Return Item")
                # Add a label for the reference number
                tk.Label(return_item_window, text="Enter the reference number:").pack()
                # Add an entry field for the reference number
                reference_number_entry = tk.Entry(return_item_window)
                reference_number_entry.pack()
                # Add a label for the item quantity
                tk.Label(return_item_window, text="Enter the item quantity:").pack()
                # Add an entry field for the item quantity
                quantity_entry = tk.Entry(return_item_window)
                quantity_entry.pack()
                # Add a button to confirm the return
                tk.Button(return_item_window, text="Confirm",
                          command=lambda: confirm_return_item(reference_number_entry.get(),
                                                              quantity_entry.get())).pack()
return_item()

              # Confirm the return of the item
def confirm_return_item(reference_number, quantity):
                # Check if the reference number exists
                cursor.execute("SELECT * FROM invoices WHERE reference_number=?", (reference_number,))
                invoice = cursor.fetchone()
                if invoice:
                  # If the reference number exists, get the item code and the item quantity
                  code = invoice[1]
                  invoice_quantity = invoice[2]
                  # Check if the item code exists
                  cursor.execute("SELECT * FROM items WHERE code=?", (code,))
                  item = cursor.fetchone()
                  if item:
                    # If the item code exists, increase the quantity in the database
                    cursor.execute("UPDATE items SET quantity=? WHERE code=?", (item[2] + int(quantity),code))
                    #Generate a random return reference number
                    return_reference_number=''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
confirm_return_item()

#defining return reference number
def return_reference_number():
    #Check if return reference number exists
    cursor.execute("SELECT * FROM invoices WHERE reference_number=?", (return_reference_number,))
    invoice = cursor.fetchone()
    if invoice:
       #If the reference number exisits, get the item code and the item quantity
       code= invoice[1]
       invoice_quantity=invoice[2]
       #Check if the item code exists
       cursor.execute("SELECT * FROM items WHERE code=?",(code,))
       item=cursor.fetchone()
       if item:
         # If the item code exists, increase the quantity in the database
         cursor.execute("UPDATE items SET quantity=? WHERE code=?", (item[2] + int(quantity), code))
         #Generate a random return reference number
         return_reference_number=''.join(random.choices(string.ascii+ string.digits, k=10))
return_reference_number()

#defining reference number
def reference_number():
    # Check if return reference number exists
    cursor.execute("SELECT * FROM invoices WHERE reference_number=?", (reference_number,))
    invoice = cursor.fetchone()
    if invoice:
       #If the reference number exisits, get the item code and the item quantity
       code= invoice[1]
       invoice_quantity=invoice[2]
       #Check if the item code exists
       cursor.execute("SELECT * FROM items WHERE code=?",(code,))
       item=cursor.fetchone()
       if item:
         # If the item code exists, increase the quantity in the database
         cursor.execute("UPDATE items SET quantity=? WHERE code=?", (item[2] + int(quantity), code))
         #Generate a random return reference number
         reference_number=''.join(random.choices(string.ascii+ string.digits, k=10))
reference_number()

#dictionary to store information and defining quantity
items = {}

def set_quantity(item_name, item_quantity):
    # assign the quantity to the item
    items[item_name] = {"quantity": item_quantity}

# define some items and their quantities
set_quantity("t-shirt", 50)
set_quantity("jeans", 40)
set_quantity("hat", 20)

# print the quantity of t-shirts
print(items["t-shirt"]["quantity"]) # Output: 50

class ClothingItem:
    def __init__(self, name):
        self.name = name
        self.quantity = 0
set_quantity()
def set_quantity(clothing_item, item_quantity):
    # assign the quantity to the item
    clothing_item.quantity = item_quantity

tshirt = ClothingItem("T-Shirt")
jeans = ClothingItem("Jeans")
hat = ClothingItem("Hat")

set_quantity(tshirt, 50)
set_quantity(jeans, 40)
set_quantity(hat, 20)

print(tshirt.quantity)  # Output: 50
set_quantity()


# Generate the QR code for the return
img = qrcode.make(return_reference_number)


# Log out
def logout():
# Clear the session
    session.clear()
# Destroy the main window
    window.destroy()
# Create a new login window
    login_window = tk.Tk()
    login_window.title("Login")
  # Add a label for the email
    tk.Label(login_window, text="Enter your email:").pack()
  # Add an entry field for the email
    email_entry = tk.Entry(login_window)
    email_entry.pack()
  # Add a label for the password
    tk.Label(login_window, text="Enter your password:").pack()
  # Add an entry field for the password
    password_entry =tk.Entry(login_window, show="*")
    password_entry.pack()
# Add a button to login
    tk.Button(login_window, text="Login", command=lambda: login(email_entry.get(), password_entry.get(), login_window)).pack()
# Run the login window
    login_window.mainloop()
logout()


# Create the main window
window = tk.Tk()
window.title("Fashion Resolutions")
window.title()

# Add a label to welcome the user
welcome_label = tk.Label(window, text="Welcome to Fashion Resolutions")
welcome_label.pack()

# Add a label to display success messages
success_label = tk.Label(window)
success_label.pack()

# Add a label to display error messages
error_label = tk.Label(window, fg="red")
error_label.pack()


# Run the main window
window.mainloop()

# Close the database connection
conn.close()