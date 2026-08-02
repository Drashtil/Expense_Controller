data = []
try:
    with open("expenses.text","r") as f:
        for line in f:
            data.append(line.strip())
except:
    pass
def save_expense():
    with open("expenses.text","w") as f:
        for expense in data:
            f.write(expense + "\n")
def add_expenses():
    amt = input("Enter your amount: ")
    category = input("Enter your catgory: ")
    expense = amt+":"+category
    data.append(expense)
    print("Your Expenses are added successfully")
    save_expense()
def view_expense():
    for d in data:
        print(d)
    
def total_spending():
    total=0
    for d in data:
        amt = int(d.split(":")[0])
        total += amt
    print("Your total spending = ",total)

    
def category_summary():
    summary = {}
    for i in data:
        category = i.split(":")[1]
        amt = int(i.split(":")[0])
        if category in summary:
            summary[category] += amt
        else:
            summary[category] = amt
    print(summary)
while True:
    print("1.add expense")
    print("2.viw expense")
    print("3.total spending")
    print("4.categoy summary")
    print("5.exit")
    choice = int(input("Enter your choice: "))
    if(choice == 1):
        add_expenses()
    elif(choice==2):
        view_expense()
    elif(choice==3):
        total_spending()
    elif(choice==4):
        category_summary()
    elif(choice==5):
        break
    else:
        print("Invalid choice")
        continue
