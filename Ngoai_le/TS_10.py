import time
import random

class StudentAdmissionSystem:
    def __init__(self):
        print("=== CHƯƠNG TRÌNH TÍNH ĐIỂM CHUẨN ĐẬU VÀO TRƯỜNG CẤP 3 ===\n")
        time.sleep(1)
        self.nguyen_vong = []

    def generate_captcha(self):
        captcha = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=7))
        print('Hãy nhập theo CAPTCHA sau đây: ' + captcha)
        user_input = input('Nhập nó ở đây -->: ')
        return user_input == captcha

    def login(self):
        print(" === VUI LÒNG ĐĂNG NHẬP === ")
        while True:
            if self.generate_captcha():
                username = input('Nhập tên tài khoản: ')
                password = input('Nhập mật khẩu tài khoản: ')
                if username == 'student1' and password == 'password1':
                    print('Đăng nhập thành công')
                    break
                else:
                    print('Đăng nhập không thành công')

    def input_student_info(self):
        print(" === Vui lòng nhập thông tin thí sinh === ")
        self.so_bao_danh = input("Nhập số báo danh: ")
        self.ten = input("Nhập họ và tên: ")
        self.tinh_thanh = input("Nhập tỉnh/ Thành phố: ")
        self.truong_du_thi = input("Nhập tên trường dự thi: ")
        self.phong_du_thi = input("Nhập số phòng dự thi: ")

    def input_scores(self):
        print("="*50)
        print("\n=== ĐIỂM MÔN THƯỜNG ===")
        print(" === Vui lòng nhập điểm từng môn === ")
        self.toan = self.get_valid_score("Toán")
        self.van = self.get_valid_score("Văn")
        self.anh = self.get_valid_score("Anh")

    def get_valid_score(self, subject):
        while True:
            score = float(input(f"Nhập điểm môn {subject}: "))
            if 0 <= score <= 10:
                return score
            else:
                print(f"Điểm môn {subject} không hợp lệ. Vui lòng nhập lại!")

    def input_specialized_subject(self):
        print("="*50)
        print("=== ĐIỂM MÔN CHUYÊN ===")
        print("Chọn môn chuyên của bạn:")
        print("1. Toán")
        print("2. Văn")
        print("3. Anh")
        choices = {'1': 'Toán', '2': 'Văn', '3': 'Anh'}
        while True:
            choice = input("Nhập lựa chọn của bạn (1-3): ")
            if choice in choices:
                self.ten_mon_chuyen = choices[choice]
                self.diem_mon_chuyen = float(input(f"Nhập điểm môn {self.ten_mon_chuyen}: "))
                break
            else:
                print("Lựa chọn không hợp lệ. Vui lòng nhập lại (1-3): ")

    def input_desired_schools(self):
        print("="*50)
        print("=== NGUYỆN VỌNG VÀ ĐIỂM CHUẨN ===")
        for i in range(3):
            ten_nv = input(f"Nhập tên trường nguyện vọng {i+1}: ")
            diem_chuan_nv = float(input(f"Nhập điểm chuẩn nguyện vọng {i+1}: "))
            self.nguyen_vong.append({"ten": ten_nv, "diem_chuan": diem_chuan_nv})

    def calculate_total_score(self):
        return self.toan + self.van + self.anh + (self.diem_mon_chuyen * 2)

    def check_admission(self):
        tong_diem = self.calculate_total_score()
        print("="*50)
        print("\n=== THÔNG TIN - KẾT QUẢ THI ===")
        print(f"Số báo danh: {self.so_bao_danh}")
        print(f"Họ và tên: {self.ten}")
        print(f"Tỉnh/ Thành phố: {self.tinh_thanh}")
        print(f"Trường dự thi: {self.truong_du_thi}")
        print(f"Số phòng dự thi: {self.phong_du_thi}")
        print(f"Điểm môn chuyên: {self.diem_mon_chuyen}")
        print(f"Điểm tổng: {tong_diem}")

        for i, nv in enumerate(self.nguyen_vong):
            print(f"Nguyện vọng {i+1}: {nv['ten']} (Điểm chuẩn: {nv['diem_chuan']})")
            if tong_diem >= nv["diem_chuan"]:
                print(f"Kết quả xét tuyển: Đậu nguyện vọng {i+1}!")
                break
        else:
            print("Kết quả xét tuyển: Không đậu vào bất kỳ nguyện vọng nào!")
            print("Hẹn gặp bạn vào kì thi năm sau, chúc may mắn!")

    def calculate_score_difference(self):
        for nv in self.nguyen_vong:
            chenh_lech = nv["diem_chuan"] - self.calculate_total_score()
            print(f"Điểm chênh lệch với nguyện vọng {nv['ten']}: {chenh_lech}")

    def sort_desired_schools(self):
        self.nguyen_vong.sort(key=lambda x: x["diem_chuan"], reverse=True)
        print("\n=== THÔNG TIN NGUYỆN VỌNG ===")
        for i, nv in enumerate(self.nguyen_vong):
            print(f"{i+1}. {nv['ten']} (Điểm chuẩn: {nv['diem_chuan']})")

    def run(self):
        self.login()
        self.input_student_info()
        self.input_scores()
        self.input_specialized_subject()
        self.input_desired_schools()
        self.check_admission()
        self.calculate_score_difference()
        self.sort_desired_schools()

if __name__ == "__main__":
    admission_system = StudentAdmissionSystem()
    admission_system.run()
