import csv
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

FILE = "expenses.csv"

# Initialize CSV file if not exists
def init_file():
    try:
        with open(FILE, "x") as f:
            f.write("Date,Category,Amount\n")
    except FileExistsError:
        pass

def add_expense():
    category = category_entry.get()
    amount = amount_entry.get()

    if not category or not amount:
        messagebox.showerror("Error", "Please enter both category and amount")
        return

    try:
        amt = float(amount)
    except ValueError:
        messagebox.showerror("Error", "Amount must be a number")
        return

    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now().strftime("%Y-%m-%d"), category, amt])
    messagebox.showinfo("Success", f"Added ₹{amt} to {category}")

    category_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)

def view_summary():
    expenses = {}
    total = 0

    with open(FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            cat = row["Category"]
            amt = float(row["Amount"])
            expenses[cat] = expenses.get(cat, 0) + amt
            total += amt

    summary = "📊 Expense Summary:\n\n"
    for cat, amt in expenses.items():
        percent = (amt / total) * 100 if total > 0 else 0
        bar = "█" * int(percent // 2)
        summary += f"{cat}: ₹{amt} ({percent:.1f}%) {bar}\n"

    summary += f"\n💰 Total Spent: ₹{total}"
    messagebox.showinfo("Summary", summary)

# GUI setup
init_file()
root = tk.Tk()
root.title("Expense Tracker")

tk.Label(root, text="Category:").grid(row=0, column=0, padx=5, pady=5)
category_entry = tk.Entry(root)
category_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Amount:").grid(row=1, column=0, padx=5, pady=5)
amount_entry = tk.Entry(root)
amount_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Button(root, text="Add Expense", command=add_expense).grid(row=2, column=0, padx=5, pady=5)
tk.Button(root, text="View Summary", command=view_summary).grid(row=2, column=1, padx=5, pady=5)

root.mainloop()
