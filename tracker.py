import csv
from datetime import datetime

FILE = "expenses.csv"

# Initialize CSV file if not exists
def init_file():
    try:
        with open(FILE, "x") as f:
            f.write("Date,Category,Amount\n")
    except FileExistsError:
        pass

def add_expense(category, amount):
    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now().strftime("%Y-%m-%d"), category, amount])
    print(f"Added ₹{amount} to {category}")

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

    print("\n Expense Summary:")
    for cat, amt in expenses.items():
        percent = (amt / total) * 100 if total > 0 else 0
        bar = "█" * int(percent // 2)  # ASCII bar chart
        print(f"{cat}: ₹{amt} ({percent:.1f}%) {bar}")

    print(f"\n Total Spent: ₹{total}")

def main():
    init_file()
    while True:
        print("\n1. Add Expense\n2. View Summary\n3. Exit")
        choice = input("Choose: ")
        if choice == "1":
            category = input("Enter category (Food/Travel/Other): ")
            amount = input("Enter amount: ")
            add_expense(category, amount)
        elif choice == "2":
            view_summary()
        elif choice == "3":
            print(" see u next time")
            break
        else:
            print(" Invalid choice!")

if __name__ == "__main__":
    main()

