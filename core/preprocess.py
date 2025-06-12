import re
import string
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory


# Stopword remover
stop_factory = StopWordRemoverFactory()
stopwords = stop_factory.get_stop_words()

# Stemmer
factory = StemmerFactory()
stemmer = factory.create_stemmer()


def preprocess_text(text):
    # 1. Lowercase
    text = text.lower()

    # 2. Remove link/url
    text = re.sub(r"http\S+|www\S+|https\S+", '', text, flags=re.MULTILINE)

    # 3. Remove angka dan tanda baca
    text = re.sub(r'[^a-zA-Z\s]', '', text)

    # 4. Remove whitespaces ganda
    text = re.sub(r'\s+', ' ', text).strip()

    # 5. Remove stopwords
    text = ' '.join([word for word in text.split() if word not in stopwords])

    # 6. Stemming
    # text = stemmer.stem(text)

    return text
