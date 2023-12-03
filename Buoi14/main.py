canh_1 = int(input("Hãy nhập chiều dài cạnh 1: "))
canh_2 = int(input("Hãy nhập chiều dài cạnh 2: "))
canh_3 = int(input("Hãy nhập chiều dài cạnh 3: "))

if canh_1 < canh_2 + canh_3:
    print("đây không là tam giác")
elif canh_1 == canh_2 == canh_3:
    print("Đây là tam giác đều")
elif canh_1 == canh_2:
    print("Đây là tam giác cân")
elif canh_1**2 == canh_2**2 + canh_3**2:
    print("Đây là tam giác vuông")
else:
    print("Đây là tam giác thường")
    