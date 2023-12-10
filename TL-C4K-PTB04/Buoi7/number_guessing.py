import random

number = random.randint(1, 100)
guess = None
attempts = 0

print("Chào mừng đến với trò chơi Number Guessing!")

while guess != number:
    guess = int(input("Nhập một số từ 1 đến 100: "))
    attempts += 1

    if guess < number:
        print("Số bạn đoán nhỏ hơn số cần tìm. Hãy đoán lại!")
    elif guess > number:
        print("Số bạn đoán lớn hơn số cần tìm. Hãy đoán lại!")
    else:
        print(f"Chúc mừng! Bạn đã đoán đúng số {number} sau {attempts} lần đoán.")
        break

print("Cảm ơn bạn đã tham gia trò chơi!")