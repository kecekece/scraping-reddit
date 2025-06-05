import praw
import pandas as pd
import datetime

# Konfigurasi PRAW
# clienId = 'PSuaWDRRg4ObgnwsdlynHQ'
# clientSecret = 'DyLWAJ9wFteIAYqblT1o9Pq-1pwL1A'
# userAgent = 'script:hate-speech-detector:v1.0 (by u/bubbob2)'
clienId = '-e2UMkfFVaoEdqICyI9v5Q'
clientSecret = 'rquMZp_C9LQgvXEjqAhH8mblZEOQ5A'
userAgent = 'script:hate-speech-detector:v1.0 (by u/gunz123_)'

def getRedditData(redditUrl: str):
    reddit = praw.Reddit(
        client_id=clienId,
        client_secret=clientSecret,
        user_agent=userAgent,
    )

    # Ambil submission dari subreddit
    # subreddit = reddit.subreddit('indonesia')  # Ganti sesuai kebutuhan
    # urlLink = 'https://www.reddit.com/r/indonesia/comments/bsimrn/prediksi_saya_mengenai_perpolitikan_indonesia/'
    # urlLink = 'https://www.reddit.com/r/indonesia/comments/1h6a0a5/asli_kasus_terplot_twist_tahun_ini_udah_curiga/'

    submission = reddit.submission(url=redditUrl)  # Ganti sesuai kebutuhan

    tanngalPostingan = datetime.datetime.fromtimestamp(submission.created_utc)

    # if(tanngalPostingan.year > 2021 and tanngalPostingan.year < 2024) :
    if(tanngalPostingan.year > 2021) :
        submission.comments.replace_more(limit=0)
        comments = submission.comments.list()  


        # Simpan komentar
        komentar_list = []

        for comment in comments:
            komentar_list.append({
                'id' : comment.id,
                'author' : str(comment.author),
                'body' : comment.body,
                'created_at' : (datetime.datetime.fromtimestamp(comment.created_utc)).strftime('%Y-%m-%d %H:%M:%S'),
            })
        return komentar_list

        # Simpan ke CSV
        df = pd.DataFrame(komentar_list)
        df.to_excel('komentar_reddit.xlsx', index=False)
        # print("Komentar berhasil disimpan ke komentar_reddit.csv")

    else:
        raise ValueError("Tahun tidak sesuai")
