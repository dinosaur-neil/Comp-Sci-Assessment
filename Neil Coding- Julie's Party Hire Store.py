from tkinter import *
import sqlite3


root = Tk()
root.title('Julies Party Hire Store')
root.geometry("400x400")

# Databases

# Create a database or connect to one
conn = sqlite3.connect('address_book.db')

# Create cursor
c = conn.cursor()

# Create table



#Commit changes
conn.commit()

# Close Connection
conn.close()

root.mainloop()