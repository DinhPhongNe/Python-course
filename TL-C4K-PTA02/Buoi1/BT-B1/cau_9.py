def xac_dinh_thoi_gian(time_str):
    danh_sach_thoi_gian = time_str.split(":") 
    
    if len(danh_sach_thoi_gian) != 3:
        return False
    
    try:
        gio = int(danh_sach_thoi_gian[0])
        phut = int(danh_sach_thoi_gian[1])
        giay = int(danh_sach_thoi_gian[2])
        
        if 0 <= gio <= 23 and 0 <= phut <= 59 and 0 <= giay <= 59:
            return True
        else:
            return False
    except ValueError:
        return False

nhap = input("Nhập giờ, phút và giây theo định dạng hh:mm:ss: ")
if xac_dinh_thoi_gian(nhap):
    print("Thời gian hợp lệ!")
else:
    print("Thời gian không hợp lệ. Vui lòng kiểm tra lại định dạng.")
