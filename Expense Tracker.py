#Expense Tracker
def get_expense():
    choice ="yes"
    Expense = []
    while (choice=="yes"):
        try:
            cat = input("Enter the category of the expense:")
            exp = float(input("Enter the expense you made: "))
        except ValueError:
            print("Please enter a numeric value")
            continue
        choice = input("Do you want to add more expense? yes/no: ").lower()
        d={
            "Category": cat,
            "Expense": exp
        }
        Expense.append(d)
    return Expense

def store_expense(Expense):
    f=open("Expenses.txt","w")
    f.write(str(Expense))
    f.close()

def show_expense():
    f=open("Expenses.txt","r")
    print(f.read())
    f.close()

def Total_expense(Expense):
    total=0
    for items in Expense:
        total+=items["Expense"]
    print("Your Total Expense is: ",total)

Expense = get_expense()
store_expense(Expense)
show_expense()
Total_expense(Expense)
