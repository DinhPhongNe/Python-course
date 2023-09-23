print("---------------------===nhận diện cảm xúc qua văn bản===---------------------")
from textblob import TextBlob

# Hàm phân tích cảm xúc
def analyze_sentiment(text):

  analysis = TextBlob(text)

  sentiment = analysis.sentiment

  print("Cảm xúc trung bình: ", sentiment.polarity)

  if sentiment.polarity == 0:
    print("Trung tính")
  elif sentiment.polarity > 0:
    print("Tích cực") 
  else:
    print("Tiêu cực")

  print("Cấp độ cảm xúc: ", sentiment.subjectivity)

# Main
print("HỆ THỐNG PHÂN TÍCH CẢM XÚC TỪ VĂN BẢN")

while True:

  text = input("Nhập văn bản: ")

  analyze_sentiment(text)

  cont = input("Tiếp tục? (Y/N)")

  if cont.upper() == "N":
    break