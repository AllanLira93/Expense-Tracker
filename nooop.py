print("Welcome to the expense tracker!")
import json
filename = "expenses.json"
try:
    with open(filename, "r", encoding="utf-8") as file:
        expense = json.load(file)
except FileNotFoundError:
    expense = {}

def save_expenses():
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(expense, file, ensure_ascii=False,  indent=4)
def add_expenses():
    item = (input("Please enter the item you wish to add: "))
    try:
        expense[item] = float(input("Please enter the amount you want to add: "))
        save_expenses()
    except ValueError:
        print("Invalid price! Please enter a number.")
    return expense

def view_expenses():
    print("Showing expenses: ")
    if not expense:
        print("No expenses recorded yet!")
    else:
        for item, value in expense.items():
            print(item, ": ", expense[item])

def sum_expenses():
    print("Summing expenses: ")
    if not expense:
        print("No expenses at the moment!")
    else:
        total = sum(expense.values())
        print(f"Total expense: {total:.2f}")

def menu():
    while True:
        print(("Please enter the number corresponding to your desired option: "))
        print("1_ Add expenses")
        print("2_ View expenses")
        print("3_ Show total expense")
        print("4_ Exit")

        try:
            options = int(input("Option: "))
        except ValueError:
            print("Invalid input! Please enter a number (1, 2 or 3).")
            continue

        if options == 1:
            add_expenses()

        elif options == 2:
            view_expenses()

        elif options == 3:
            sum_expenses()

        elif options == 4:
            print("Program completed!")
            break
        else:
            print("Please enter a valid option")

menu()

