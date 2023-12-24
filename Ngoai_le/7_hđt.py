from sympy import symbols, expand

print("---------------------===Giải 7 hằng đẳng thức===---------------------")

print("1. (A + B)^2 = A^2 + 2AB + B^2")
print("2. (A - B)^2 = A^2 - 2AB + B^2")
print("3. A^2 - B^2 = (A - B)(A + B)")
print("4. (A + B)^3 = A^3 + 3.A^2.B + 3.A.B^2 + B^3")
print("5. (A - B)^3 = A^3 - 3.A^2.B + 3.A.B^2 - B^3")
print("6. A^3 + B^3 = (A + B)(A^2 - AB + B^2)")
print("7. A^3 - B^3 = (A - B)(A^2 + AB + B^2)")

hdt_select = int(input("Hãy chọn 1 trong 7 hằng đẳng thức ở trên: "))

# Khai báo biến chữ cái
A, B = symbols('A B')

he_a = input("Hãy nhập vào biến A của hằng đẳng thức bạn chọn (ví dụ: 2*x): ")
he_b = input("Hãy nhập vào biến B của hằng đẳng thức bạn chọn (ví dụ: 3*y): ")

# Thay thế các biến chữ cái bằng biểu thức sympy
he_a_expr = eval(he_a.replace('*', ''))
he_b_expr = eval(he_b.replace('*', ''))

# Tạo biểu thức hằng đẳng thức dựa trên lựa chọn của người dùng
if hdt_select == 1:
    hdt_expr = (A + B)**2
elif hdt_select == 2:
    hdt_expr = (A - B)**2
elif hdt_select == 3:
    hdt_expr = A**2 - B**2
elif hdt_select == 4:
    hdt_expr = (A + B)**3
elif hdt_select == 5:
    hdt_expr = (A - B)**3
elif hdt_select == 6:
    hdt_expr = A**3 + B**3
elif hdt_select == 7:
    hdt_expr = A**3 - B**3
else:
    print("Không có hằng đẳng thức nào như vậy")
    exit()

# Thay thế biến chữ cái trong hằng đẳng thức
hdt_expr = hdt_expr.subs([(A, he_a_expr), (B, he_b_expr)])

# Khai triển hằng đẳng thức
expanded_expr = expand(hdt_expr)

# In ra từng bước khai triển
print("Kết quả sau khi khai triển với hệ số A là {} và hệ số B là {} là:".format(he_a, he_b))
print("Hằng đẳng thức ban đầu: {}".format(hdt_expr))
print("Khai triển hằng đẳng thức: {}".format(expanded_expr))
