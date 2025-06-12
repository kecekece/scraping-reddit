import praw
import prawcore
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from core.preprocess import preprocess_text

try:
    clienId = '-e2UMkfFVaoEdqICyI9v5Q'
    clientSecret = 'rquMZp_C9LQgvXEjqAhH8mblZEOQ5A'
    userAgent = 'script:hate-speech-detector:v1.0 (by u/gunz123_)'

    reddit = praw.Reddit(client_id=clienId, client_secret=clientSecret, user_agent=userAgent)
    reddit.read_only = True
    comments = reddit.subreddit('indonesia').comments(limit=2000)

    komentar_list = []

    for comment in comments:
        komentar_list.append(preprocess_text(comment.body))
    filteredComments = [comment for comment in komentar_list if comment.strip() != '']
    df = pd.DataFrame(filteredComments)

    # headers= ['id', 'authora', 'comment', 'preproses']
    df.to_excel('data_komentar.xlsx', index=False)

    # vectorizer = TfidfVectorizer()
    # X = vectorizer.fit_transform(komentar_list)
    # print("Bentuk fitur (baris: dokumen, kolom: kata unik):", X.shape)
    # print("Fitur kata:", vectorizer.get_feature_names_out())

    # df_fitur = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())
    # df_fitur.to_excel('komentar_reddit2.xlsx', index=False)
    # print(df_fitur)



    # print(komentar_list)

    # Simpan ke CSV
    # df = pd.DataFrame(komentar_list)
    # headers= ['id', 'author', 'comment', 'preproses']
    # df.to_excel('komentar_reddit2.xlsx', index=False)
    # print("Komentar berhasil disimpan ke komentar_reddit.csv")
except prawcore.exceptions.OAuthException:
    print("Token OAuth tidak valid.")
except prawcore.exceptions.ResponseException as e:
    if e.response.status_code == 401:
        print("401 Unauthorized: Periksa client_id dan client_secret.")
    else:
        print(f"Terjadi error lain: {e}")