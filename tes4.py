# from transformers import AutoTokenizer, AutoModelForSequenceClassification
# import torch
# import pandas as pd

# # Load file komentar
# df = pd.read_excel('data_komentar.xlsx', header=None)
# df.columns = ['komentar']


# # Muat model IndoBERT hate speech (jika tersedia di HF)
# model_name = "w11wo/indonesian-hatespeech-classification"  # Ganti dengan model yang cocok
# tokenizer = AutoTokenizer.from_pretrained(model_name)
# model = AutoModelForSequenceClassification.from_pretrained(model_name)

# # Fungsi prediksi
# def prediksi_komentar(text):
#     inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
#     outputs = model(**inputs)
#     probs = torch.nn.functional.softmax(outputs.logits, dim=1)
#     label = torch.argmax(probs).item()
#     return label  # misalnya 1 = hate speech, 0 = bukan

# # def cetak(text):
# #     print(text)
# # Terapkan ke semua komentar
# df['label'] = df['komentar'].apply(prediksi_komentar)

# # Simpan hasil
# df.to_excel('hasil_label_otomatis.xlsx', index=False)



import pandas as pd
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load data
file_path = "data_komentar.xlsx"
df = pd.read_excel(file_path, header=None)
df.columns = ['komentar']

# Pastikan kolom 'komentar' ada
if 'komentar' not in df.columns:
    raise ValueError("Kolom 'komentar' tidak ditemukan dalam file Excel.")

# Load tokenizer dan model dari Hugging Face
model_name = "OwLim/indonesian-roberta-hate-speech-detection"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Mapping label output
label_map = {1: "hate_speech", 0: "non_hate_speech"}

# Fungsi prediksi label (biner: hate_speech = 1, lainnya = 0)
def prediksi_label_biner(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    outputs = model(**inputs)
    probs = torch.nn.functional.softmax(outputs.logits, dim=1)
    pred = torch.argmax(probs, dim=1).item()
    return 0 if pred == 0 else 1  # 1 = hate_speech, 0 = bukan

# Terapkan ke semua komentar
df['label'] = df['komentar'].astype(str).apply(prediksi_label_biner)

# Simpan hasil
output_path = "data_komentar_berlabel.xlsx"
df.to_excel(output_path, index=False)

output_path
