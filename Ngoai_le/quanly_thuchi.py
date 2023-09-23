print("---------------------===Quản lý thu chi===---------------------")
import datetime

# Danh sách các khoản thu chi
expenses = [] 
incomes = []

# Hàm thêm khoản thu
def add_income():
    title = input("Nội dung: ")
    amount = float(input("Số tiền: "))
    date = datetime.datetime.now()

    income = {
        "title": title,
        "amount": amount, 
        "date": date
    }

    incomes.append(income)
    print("Khoản thu đã được thêm thành công.")

# Hàm thêm khoản chi  
def add_expense():
    title = input("Nội dung: ") 
    amount = float(input("Số tiền: "))
    date = datetime.datetime.now()

    expense = {
        "title": title,
        "amount": amount,
        "date": date
    }

    expenses.append(expense)
    print("Khoản chi đã được thêm thành công.")

# Hàm hiển thị báo cáo thu chi
def show_report():
    print("\nBÁO CÁO THU CHI")
    print("--------------------------------------------------")
    
    total_income = sum(income["amount"] for income in incomes)
    total_expense = sum(expense["amount"] for expense in expenses)
    balance = total_income - total_expense
    
    print("Tổng thu      : ", total_income)
    print("Tổng chi      : ", total_expense)
    print("Số dư hiện tại: ", balance)

    print("\nDanh sách khoản thu:")
    for income in incomes:
        print(income["title"], ", Số tiền:", income["amount"], ", Ngày:", income["date"])

    print("\nDanh sách khoản chi:")
    for expense in expenses:
        print(expense["title"], ", Số tiền:", expense["amount"], ", Ngày:", expense["date"])

# Hiển thị menu
print("QUẢN LÝ THU CHI")
while True:
    print("1. Thêm khoản thu") 
    print("2. Thêm khoản chi")
    print("3. Xem báo cáo")
    print("4. Thoát")

    option = int(input("Lựa chọn: "))

    if option == 1:
        add_income()
    elif option == 2:    
        add_expense()
    elif option == 3:
        show_report()
    elif option == 4:
        break
    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")