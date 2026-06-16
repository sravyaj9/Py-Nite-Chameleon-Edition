# Expense tracker
expense={}
def add_expense(item,amount):
    expense1={item:amount}
    expense.update(expense1)
    print((f"{item}expense is added"))

def view_expense():
    print("expense list:",expense)

def total_expense():
     total=sum(expense.values())
     print(f"total expense is {total}")

while True:
    print("welcome to expense tracker")
    print("enter 1 for add expense")
    print("enter 2 for view expense")
    print("enter 3 for total expense")
    print("enter 4 to exit")
    choice=int(input("enter your choice:"))
    if choice==1:
        item=input("enter the item you want to add:")
        amount=int(input("enter the amount you want to add:"))
        add_expense(item,amount)
    if choice==2:
        view_expense()
    if choice==3:
        total_expense()
    if choice==4:
        print("Thank you for using the expense tracker!, Bye")
        break
