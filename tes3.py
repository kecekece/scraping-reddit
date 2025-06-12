import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer


# Membaca file Excel
df = pd.read_excel("data_komentar.xlsx")
# Ganti 'Komentar' dengan nama kolom yang benar jika berbeda
df = df.dropna(subset=[df.columns[0]])

# Ambil kolom komentar sebagai list dan filter string kosong
comments = df.iloc[:, 0].astype(str).tolist()
comments = [comment for comment in comments if comment.strip() != '']

# print(comments)

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(comments)
print("Bentuk fitur (baris: dokumen, kolom: kata unik):", X.shape)
print("Fitur kata:", vectorizer.get_feature_names_out())

df_fitur = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())
df_fitur.to_excel('vectorizer.xlsx', index=False)
print(df_fitur)