# ==========-------- CODE RUNNER - CHẠY TRẠM --------==========

#Trạm 1:
print("==============Trạm 1==============")
print("=> Yêu cầu: viết chương trình tín tổng có sẵn trong 1 danh sách các số nguyên")

def tinh_tong_danh_sach(danh_sach):
    tong = sum(danh_sach)
    return tong

# ví dụ sử dụng hàm:
danh_sach = [1,2,3,4,5,6,7,8,9,10]
ket_qua = tinh_tong_danh_sach(danh_sach)
print(f"Tổng các phần tử trong danh sách là {ket_qua}")



#Trạm 2:
print("==============Trạm 2==============")
print("=> Yêu cầu: viết chương trình loại bỏ các phần tử trùng nhau trong danh sách")
def loai_bo_trung(lst):
    return list(set(lst))

# Ví dụ sử dụng
danh_sach = [1, 2, 2, 3, 4, 4, 5]
danh_sach_moi = loai_bo_trung(danh_sach)

print("Danh sách ban đầu:", danh_sach)
print("Danh sách sau khi loại bỏ phần tử trùng nhau:", danh_sach_moi)



#Trạm 3:
print("==============Trạm 3==============")
print("=> Yêu cầu: viết chương trình kiểm tra xem một chuỗi nhập vào có đối xứng hay không.")
def la_chuoi_doi_xung(chuoi):
    chuoi = chuoi.lower()  # Chuyển đổi chuỗi về chữ thường để không phân biệt chữ hoa và chữ thường
    return chuoi == chuoi[::-1]

# Nhập chuỗi từ người dùng
chuoi_nhap = input("Nhập một chuỗi: ")

# Kiểm tra và in kết quả
if la_chuoi_doi_xung(chuoi_nhap):
    print("Chuỗi là chuỗi đối xứng.")
else:
    print("Chuỗi không phải là chuỗi đối xứng.")
    