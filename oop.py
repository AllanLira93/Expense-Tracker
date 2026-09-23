import json

class Expense:
    def __init__(self, filename = "expense.json"):
        self.filename = filename
        self.expense = self.load_expense()

    def add_expense(self, item, price):
        self.expense.append({"item": item.upper(), "price": float(price)})
        self.save_expense()
        print("Expense added!")

    def view_expense(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                expense = json.load(file)
            if not expense:
                print("No expense")
            else:
                print("your expenses:")
                for item in self.expense:
                    print(f"Item: {item['item']}, Price: {item['price']:.2f}")
        except FileNotFoundError:
            print("Expense file not found. Add some expenses first!")

    def sum_expense(self):
        if not self.expense:
            print("No expense")
        else:
            total = sum(item["price"] for item in self.expense)
            print(f"Total expense: {total:.2f}")

    def save_expense(self):
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(self.expense, file, ensure_ascii=False, indent=4)

    def load_expense(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                expense = json.load(file)
                return expense
        except FileNotFoundError:
            return []

    def remove_expense(self, item):
        for espense in self.expense:
            if espense["item"] == item:
                self.expense.remove(espense)
                self.save_expense()
                print(f"Removed expense {espense['item']}")
                return
        print("Expense not found!")



def menu():
    tracker = Expense()

    while True:
        print("~~~~ Expense Tracker ~~~~")
        print(("Please enter the number corresponding to your desired option: "))
        print("1_ Add expenses")
        print("2_ View expenses")
        print("3_ Show total expense")
        print("4_ Remove expense")
        print("5_ Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice! Please enter a number.")
            continue

        if choice == 1:
            item = input("Enter item name: ")
            try:
                price = float(input("Enter price: "))
                tracker.add_expense(item, price)
            except ValueError:
                print("Invalid price! Please enter a numeric value")

        elif choice == 2:
            tracker.view_expense()
        elif choice == 3:
            tracker.sum_expense()
        elif choice == 4:
            item = input("Enter item name to remove: ")
            tracker.remove_expense(item.upper())
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice")
menu()





