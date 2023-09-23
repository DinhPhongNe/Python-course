print("---------------------===phân tích tư duy từ văn bản===---------------------")
import spacy
from textblob import TextBlob
from sklearn.feature_extraction.text import CountVectorizer
import streamlit as st

nlp = spacy.load('en_core_web_sm')

# Giao diện đầu vào
st.title("Phân tích tư duy từ văn bản")
text = st.text_area("Nhập văn bản")

# Phân tích văn bản
doc = nlp(text)
sentiment = TextBlob(text).sentiment

vectorizer = CountVectorizer()
bag_of_words = vectorizer.fit_transform(text)

# Trình bày kết quả
st.header("Kết quả phân tích")
st.write(f"Cảm xúc: {sentiment}")
st.write(f"Chủ đề: {vectorizer.get_feature_names()}")

for ent in doc.ents:
  st.write(ent.text, ent.label_)

st.write("Vậy văn bản nói về...") 

# Lưu kết quả
st.download_button("Tải báo cáo", "analysis_report.txt")