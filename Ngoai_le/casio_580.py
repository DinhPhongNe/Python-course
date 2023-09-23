print("---------------------===simple casio 580===---------------------")
import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Lỗi: Không thể chia cho 0!"
def square_root(a):
    if a >= 0:
        return math.sqrt(a)
    else:
        return "Lỗi: Số không hợp lệ!"

def power(a, b):
    return a ** b

def factorial(a):
    if a >= 0:
        return math.factorial(a)
    else:
        return "Lỗi: Số không hợp lệ!"

def percentage(a, b):
    return (a * b) / 100

def sin(a):
    return math.sin(math.radians(a))

def cos(a):
    return math.cos(math.radians(a))

def tan(a):
    return math.tan(math.radians(a))

def pi():
    return math.pi

def e():
    return math.e

# Hiển thị menu
print("MÁY TÍNH CASIO 580")
print("------------------")

while True:
    print("\nChọn chức năng:")
    print("1. Cộng")
    print("2. Trừ")
    print("3. Nhân")
    print("4. Chia")
    print("5. Căn bậc hai")
    print("6. Lũy thừa")
    print("7. Giai thừa")
    print("8. Phần trăm")
    print("9. Sin")
    print("10. Cos")
    print("11. Tan")
    print("12. Pi")
    print("13. e")
    print("14. Thoát")

    choice = int(input("Lựa chọn của bạn: "))

    if choice == 14:
        print("Kết thúc chương trình.")
        break

    if choice >= 1 and choice <= 13:
        if choice in [5, 7]:
            num = float(input("Nhập số: "))
        else:
            num1 = float(input("Nhập số thứ nhất: "))
            num2 = float(input("Nhập số thứ hai: "))

        if choice == 1:
            result = add(num1, num2)
        elif choice == 2:
            result = subtract(num1, num2)
        elif choice == 3:
            result = multiply(num1, num2)
        elif choice == 4:
            result = divide(num1, num2)
        elif choice == 5:
            result = square_root(num)
        elif choice == 6:
            result = power(num1, num2)
        elif choice == 7:
            result = factorial(int(num))
        elif choice == 8:
            result = percentage(num1, num2)
        elif choice == 9:
            result = sin(num)
        elif choice == 10:
            result = cos(num)
        elif choice == 11:
            result = tan(num)
        elif choice == 12:
            result = pi()
        elif choice == 13:
            result = e()

        print("Kết quả: ", result)
    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
        