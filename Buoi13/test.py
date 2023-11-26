def chuyen_sang_ma_nhi_phan(chuoi):
    ma_nhi_phan = ''
    for ky_tu in chuoi:
        ma_nhi_phan += bin(ord(ky_tu))[2:].zfill(8)
    return ma_nhi_phan

chuoi = input("Nhập vào một chuỗi: ")
ma_nhi_phan = chuyen_sang_ma_nhi_phan(chuoi)

while True:
    nhap = input("Nhập một số, chữ cái hoặc ký tự đặc biệt (nhập 'q' để thoát): ")
    if nhap == 'q':
        break
    if nhap.isdigit() or nhap.isalpha() or len(nhap) == 1:
        print("Mã nhị phân: ", ma_nhi_phan)
    else:
        print("Không hợp lệ! Vui lòng nhập một số, chữ cái hoặc ký tự đặc biệt.")

print("Kết thúc chương trình.")