import pandas as pd
import csv
import os
import matplotlib.pyplot as plt

expenses = []

def data_chart():
    if os.path.exists('Expenses.csv'):
        df = pd.read_csv('Expenses.csv')
    else:
        print("No data to visualize.")
        return
    
    category_totals = df.groupby('Category')['Amount'].sum()
    category_totals.plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title('Total Expenses per Category')
    plt.xlabel('Category')
    plt.ylabel('Total Amount')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def add_expense():
    amount = float(input("Enter expense amount: Rs "))
    category = input("Enter expense category: ")
    
    expenses.append({'amount': amount, 'category': category})
    print(f"Expense of ${amount} added!")

    with open('Expenses.csv', mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['Amount', 'Category'])
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow({'Amount': amount, 'Category': category})

def view_all_expenses():
    if not expenses:
        print("No expenses recorded yet.")
    else:
        print("\nAll Expenses:")
        for expense in expenses:
            print(f"Amount: rs {expense['amount']} | Category: {expense['category']}")

def total_expenses():
    total = sum(expense['amount'] for expense in expenses)
    print(f"Total Expenses: Rs {total}")

def category_summary():
    categories = {}
    for expense in expenses:
        categories[expense['category']] = categories.get(expense['category'], 0) + expense['amount']
    
    if not categories:
        print("No categories available.")
    else:
        print("\nExpenses by Category:")
        for category, total in categories.items():
            print(f"{category}: Rs {total}")

def main():
    if os.path.exists('Expenses.csv'):
        df = pd.read_csv('Expenses.csv')
        for _, row in df.iterrows():
            expenses.append({'amount': row['Amount'], 'category': row['Category']})

    while True:
        print("\n1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total Expenses")
        print("4. View Category Expense")
        print("5. Data Chart")
        print("6. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_all_expenses()
        elif choice == '3':
            total_expenses()
        elif choice == '4':
            category_summary()
        elif choice == '5':
            data_chart()
        elif choice == '6':
            print("Exiting..!")
            exit(0)
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
