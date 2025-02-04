import tkinter as tk
from tkinter import messagebox
import csv
import os

# File to store expenses
FILE_NAME = "expenses.csv"

# Function to add expense
def add_expense():
    amount = amount_entry.get().strip()
    category = category_entry.get().strip()
    description = desc_entry.get().strip()
    
    try:
        amount = float(amount)
        if amount <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid positive number for Amount!")
        return
    
    if not category:
        messagebox.showerror("Error", "Category is required!")
        return
    
    with open(FILE_NAME, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([amount, category, description])
    
    amount_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)
    desc_entry.delete(0, tk.END)
    messagebox.showinfo("Success", "Expense added successfully!")

# Function to show expenses
def show_expenses():
    if not os.path.exists(FILE_NAME):
        messagebox.showinfo("No Data", "No expenses recorded yet!")
        return
    
    with open(FILE_NAME, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        expenses = list(reader)
    
    expense_list.delete(0, tk.END)
    for expense in expenses:
        if len(expense) == 3:
            expense_list.insert(tk.END, f"{expense[0]} - {expense[1]} - {expense[2]}")

# GUI Setup
root = tk.Tk()
root.title("Expense Tracker")
root.geometry("400x500")

tk.Label(root, text="Amount:").pack()
amount_entry = tk.Entry(root)
amount_entry.pack()

tk.Label(root, text="Category:").pack()
category_entry = tk.Entry(root)
category_entry.pack()

tk.Label(root, text="Description:").pack()
desc_entry = tk.Entry(root)
desc_entry.pack()

tk.Button(root, text="Add Expense", command=add_expense).pack()
tk.Button(root, text="Show Expenses", command=show_expenses).pack()

expense_list = tk.Listbox(root, width=50, height=10)
expense_list.pack()

root.mainloop()
