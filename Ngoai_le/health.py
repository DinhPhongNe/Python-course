print("---------------------===quản lý sức khỏe (just simple)===---------------------")

print("HỆ THỐNG TƯ VẤN SỨC KHỎE")

# Dictionary chứa các câu hỏi và lời khuyên
health_advice = {"Câu hỏi 1": "Lời khuyên 1",
                 "Câu hỏi 2": "Lời khuyên 2", 
                 "Câu hỏi 3": "Lời khuyên 3"}

while True:
  
  # Hiển thị menu câu hỏi
  print("\nChọn câu hỏi:") 
  for key in health_advice.keys():
    print(key)

  question = input("Nhập câu hỏi cần tư vấn: ")

  # Kiểm tra câu hỏi có trong danh sách không
  if question in health_advice:
    print(health_advice[question])
  
  else:
    print("Xin lỗi, chúng tôi chưa có câu trả lời cho câu hỏi này.")

  print("\nTiếp tục hay thoát?")
  ans = input("Nhập T để tiếp tục hoặc Q để thoát: ")

  if ans.upper() == "Q":
    break