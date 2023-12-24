class BankAccount:
    def __init__(self, bank_name, account_holder_name, account_number, balance):
        self.bank_name = bank_name
        self.account_holder_name = account_holder_name
        self.account_number = account_number
        self.balance = balance

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Rút {amount} từ tài khoản. Số dư còn {self.balance}.")
        else:
            print("Lương tiền không hợp lệ hoặc số dư tài khoản không đủ.")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Gửi {amount} vào tài khoản. Số dư là {self.balance}.")
        else:
            print("Lượng tiền không hợp lệ.")

    def display_balance(self):
        print(f"Số dư trong tài khoản: {self.balance}")

def main():
    bank_name = input("Nhập tên ngân hàng: ")
    account_holder_name = input("Nhập tên tài khoản ngân hàng: ")
    account_number = input("Nhập số tài khoản: ")
    balance = float(input("Nhập số dư: "))
    account = BankAccount(bank_name, account_holder_name, account_number, balance)

    while True:
        print("\n1. Rút tiền\n2. Gửi tiền\n3. Xem số dư\n4. Thoát")
        choice = input("Nhập lựa chọn: ")
        if choice == "1":
            amount = float(input("Nhập số tiền muốn rút: "))
            account.withdraw(amount)
        elif choice == "2":
            amount = float(input("Nhập số tiền muốn gửi: "))
            account.deposit(amount)
        elif choice == "3":
            account.display_balance()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Lựa chọn không hợp lệ, hãy thử lại")

if __name__ == "__main__":
    main()
