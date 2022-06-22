from tkinter import *
from tkinter import ttk


root = Tk()
root.title('Julies Party Hire Store')
root.geometry("1000x500")

# Add Colours to make it look more appealing for the user of the program
style = ttk.Style()

# Pick A Theme
style.theme_use('default')

# Configure the Treeview Colours
style.configure("Treeview",
    Background="#D3D3D3",
    foreground="black",
    rowheight=25,
    feildbackground="D3D3D3")

# Change Selected rows Color
style.map('Treeview',
    background=[('selected', "#347083")])

# Create a Treeview Frame
tree_frame = Frame(root)
tree_frame.pack(pady=10)

# Create a Treeview Scrollbar so the user can scroll up and down that data table
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

# Create The Treeview
my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
my_tree.pack()

# Configure The Scrollbar
tree_scroll.config(command=my_tree.yview)

# Define The Columns
my_tree['columns'] = ("First Name", "Last Name", "ROW ID", "Receipt Number", "Item Hired", "Number of Item Hired", "Date of Hire")

# Format The Columns to show the details that are in the columns
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("First Name", anchor=W, width=140)
my_tree.column("Last Name", anchor=W, width=140)
my_tree.column("ROW ID", anchor=CENTER, width=100)
my_tree.column("Receipt Number", anchor=CENTER, width=140)
my_tree.column("Item Hired", anchor=CENTER, width=140)
my_tree.column("Number of Item Hired", anchor=CENTER, width=140)
my_tree.column("Date of Hire", anchor=CENTER, width=140)

# Create Headings To Show the title on top of the column
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("First Name", text="First Name", anchor=W)
my_tree.heading("Last Name", text="Last Name", anchor=W)
my_tree.heading("ROW ID", text="ROW ID #", anchor=CENTER)
my_tree.heading("Receipt Number", text="Receipt Number", anchor=CENTER)
my_tree.heading("Item Hired", text="Item Hired", anchor=CENTER)
my_tree.heading("Number of Item Hired", text="Number of Item Hired", anchor=CENTER)
my_tree.heading("Date of Hire", text="Date of Hire", anchor=CENTER)  

# Add Random Data to test if i'll show on the table
data = [
    ["Bobby", "Walker", 1, "292187", "Balloon", "5", "22/06/2022"],  
    ["Lily", "Solo", 2, "494932", "Candle", "20", "22/06/2022"],
    ["Scott", "Skywalker", 3, "893284", "Chair", "3", "22/06/2022"],
    ["Bob", "Walker", 4, "592187", "Balloon", "64", "22/06/2022"],  
    ["Lolly", "Solo", 5, "894932", "Candle", "11", "22/06/2022"],
    ["molly", "Walker", 6, "792187", "Balloon", "85", "22/06/2022"],  
    ["Han", "Solo", 7, "694932", "Candle", "40", "22/06/2022"],
    ["Anakin", "Skywalker", 8, "992187", "Balloon", "5", "22/06/2022"],  
    ["Sarah", "Black", 9, "497532", "Candle", "22", "22/06/2022"],
    ["Joe", "Mama", 10, "299487", "Balloon", "59", "22/06/2022"],  
    ["Harry", "poppy", 11, "423932", "Candle", "29", "22/06/2022"],
    ["Bruce", "Wayne", 12, "298787", "Balloon", "499", "22/06/2022"],  
    ["Michael", "Jackson", 13, "494332", "Candle", "200", "22/06/2022"]
    
]

# Create Striped Row Tags
my_tree.tag_configure('oddrow', background="White")
my_tree.tag_configure('evenrow', background="lightblue")

# Add the data onto the screen
global count
count = 0

for shop_detail in data:
    if count % 2 == 0:
        my_tree.insert(parent='', index='end', iid=count, text='', values=(shop_detail[0], shop_detail[1], shop_detail[2], shop_detail[3], shop_detail[4], shop_detail[5], shop_detail[6]), tags=('evenrow',))
    else:    
        my_tree.insert(parent='', index='end', iid=count, text='', values=(shop_detail[0], shop_detail[1], shop_detail[2], shop_detail[3], shop_detail[4], shop_detail[5], shop_detail[6]), tags=('oddrow',))
    # Increment counter
    count += 1


# Add Shop_detail Entry Boxes
data_frame = LabelFrame(root, text="Shop_details")   
data_frame.pack(fill="x", expand="yes", padx=20)

fn_label = Label(data_frame, text="First Name :")
fn_label.grid(row=0, column=0, padx=10, pady=10)
fn_entry = Entry(data_frame)
fn_entry.grid(row=0, column=1, padx=10, pady=10)

ln_label = Label(data_frame, text="Last Name :")
ln_label.grid(row=0, column=2, padx=10, pady=10)
ln_entry = Entry(data_frame)
ln_entry.grid(row=0, column=3, padx=10, pady=10)

id_label = Label(data_frame, text="ROW ID #")
id_label.grid(row=0, column=4, padx=10, pady=10)
id_entry = Entry(data_frame)
id_entry.grid(row=0, column=5, padx=10, pady=10)

receipt_label = Label(data_frame, text="Receipt Number :")
receipt_label.grid(row=1, column=0, padx=10, pady=10)
receipt_entry = Entry(data_frame)
receipt_entry.grid(row=1, column=1, padx=10, pady=10)

item_label = Label(data_frame, text="Item Hired :")
item_label.grid(row=1, column=2, padx=10, pady=10)
item_entry = Entry(data_frame)
item_entry.grid(row=1, column=3, padx=10, pady=10)

number_label = Label(data_frame, text="Number of Item Hired :")
number_label.grid(row=1, column=4, padx=10, pady=10)
number_entry = Entry(data_frame)
number_entry.grid(row=1, column=5, padx=10, pady=10)

date_label = Label(data_frame, text="Date Hired :")
date_label.grid(row=1, column=6, padx=10, pady=10)
date_entry = Entry(data_frame)
date_entry.grid(row=1, column=7, padx=10, pady=10)

# Add Buttons 



root.mainloop()