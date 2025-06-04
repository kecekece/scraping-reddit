import praw
import pandas as pd
import datetime

# Konfigurasi PRAW
reddit = praw.Reddit(
    client_id='PSuaWDRRg4ObgnwsdlynHQ',
    client_secret='DyLWAJ9wFteIAYqblT1o9Pq-1pwL1A',
    user_agent='script:hate-speech-detector:v1.0 (by u/bubbob2)',
)

# Ambil submission dari subreddit
# subreddit = reddit.subreddit('indonesia')  # Ganti sesuai kebutuhan
urlLink = 'https://www.reddit.com/r/indonesia/comments/bsimrn/prediksi_saya_mengenai_perpolitikan_indonesia/'
# urlLink = 'https://www.reddit.com/r/indonesia/comments/1h6a0a5/asli_kasus_terplot_twist_tahun_ini_udah_curiga/'

submission = reddit.submission(url=urlLink)  # Ganti sesuai kebutuhan

tanngalPostingan = datetime.datetime.fromtimestamp(submission.created_utc)

if(tanngalPostingan.year > 2021 and tanngalPostingan.year < 2024) :
    submission.comments.replace_more(limit=0)
    comments = submission.comments.list()  


    # Simpan komentar
    komentar_list = []

    for comment in comments:
        komentar_list.append([
            comment.id,
            str(comment.author),
            comment.body,
            (datetime.datetime.fromtimestamp(comment.created_utc)).strftime('%Y-%m-%d %H:%M:%S'),
        ])
    print(komentar_list)

    # Simpan ke CSV
    df = pd.DataFrame(komentar_list)
    df.to_excel('komentar_reddit.xlsx', index=False)
    # print("Komentar berhasil disimpan ke komentar_reddit.csv")

else:
    print("Postingan dibawah 2021")
