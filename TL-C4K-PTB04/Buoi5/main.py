print("---------------------===tính giá trị tuyệt đối===---------------------")
number = int(input("Nhập vào số nguyên: "))

if number >= 0:
    gia_tri_tuyet_doi = number
else:
    gia_tri_tuyet_doi = number * -1

print(f"Giá trị tuyệt đối của {number} là {gia_tri_tuyet_doi}")