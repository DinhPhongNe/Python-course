print("---------------------===Giải 7 hằng đẳng thức===---------------------")

print("1. (A + B)^2 = A^2 + 2AB + B^2")
print("2. (A - B)^2 = A^2 - 2AB + B^2")
print("3. A^2 - B^2 = (A - B)(A + B)")
print("4. (A + B)^3 = A^3 + 3.A^2.B + 3.A.B^2 + B^3")
print("5. (A - B)^3 = A^3 - 3.A^2.B + 3.A.B^2 - B^3")
print("6. A^3 + B^3 = (A + B)(A^2 - AB + B^2)")
print("7. A^3 - B^3 = (A - B)(A^2 + AB + B^2)")

hdt_select = int(input("Hãy chọn 1 trong 7 hằng đẳng thức ở trên: "))


he_a = float(input("Hãy nhập vào biến A của hằng đẳng thức bạn chọn: "))
he_b = float(input("Hãy nhập vào biến B của hằng đẳng thức bạn chọn: "))

if hdt_select == 1:
    result_hdt = he_a**2 + 2 * he_a * he_b + he_b**2
elif hdt_select == 2:
    result_hdt = he_a**2 - 2 * he_a * he_b + he_b**2
elif hdt_select == 3:
    result_hdt = (he_a + he_b)*(he_a - he_b)
elif hdt_select == 4:
    result_hdt = he_a**3 + 3 * he_a**2 * he_b + 3 * he_a * he_b**2 + he_b**3
elif hdt_select == 5:
    result_hdt = he_a**3 - 3 * he_a**2 * he_b + 3 * he_a * he_b**2 - he_b**3
elif hdt_select == 6:
    result_hdt = (he_a + he_b)(he_a**2 - he_a*he_b + he_b**2)
elif hdt_select == 7:
    result_hdt = (he_a - he_b)(he_a**2 + he_a*he_b + he_b**2)
else:
    print("không có hằng đẳng thức nào như vậy")
    
print(f"hằng đẳng thức số {hdt_select} với hệ số A là {he_a} và hệ số B là {he_b} có kết quả là {result_hdt}")
