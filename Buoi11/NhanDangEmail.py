email = input("hãy nhập email của bạn: ")
print(f"email bạn vừa nhập là: {email}")

if "@" in email:
  locate = email.find("@")
  username = email[:locate]
  domain = email[locate+1:]

  print("Trạng thái: email hợp lệ")
  print(f"Username email: {username}")
  print(f"Domain email: {domain}")
else:
  print("Trạng thái: email không hợp lệ")