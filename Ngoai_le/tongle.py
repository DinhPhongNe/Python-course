while True:
    a = int(input("Nhập một số để tính toán: "))
    if a > 0:
        break
    else:
        print("Nhập một số khác > 0")

tongle = 0
strtongle = "A = "
for i in range(1, a + 1):
    if i % 2 != 0:
        tongle += i
        strtongle += str(i) + "+"

ketquatongle = strtongle.rstrip("+") + "="
print(ketquatongle, tongle)