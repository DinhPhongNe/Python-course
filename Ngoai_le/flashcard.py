print("---------------------===flashcard===---------------------")
# Danh sách các bộ flashcard
flashcards = []

# Class định nghĩa cấu trúc flashcard
class Flashcard:
  def __init__(self, front, back):
    self.front = front
    self.back = back

# Hàm thêm mới flashcard  
def add_card():
  front = input("Nhập mặt trước: ")
  back = input("Nhập mặt sau: ")
  
  new_card = Flashcard(front, back)
  flashcards.append(new_card)
  
# Hàm xem flashcard   
def view_card():
  for card in flashcards:
    print(f"Mặt trước: {card.front}")
    input("Nhấn enter để xem mặt sau ...")
    print(f"Mặt sau: {card.back}")

# Main      
print("ỨNG DỤNG TẠO FLASHCARD")

while True:
  print("1. Thêm flashcard")
  print("2. Xem flashcard")
  print("3. Thoát")

  choice = int(input("Lựa chọn: "))

  if choice == 1:
    add_card()
  elif choice == 2:  
    view_card()   
  elif choice == 3:
    break