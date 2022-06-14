import re

import globe
import matplotlib.image
import pandas as pd
from matplotlib import pyplot as plt
from nltk import PorterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from wordcloud import WordCloud


def usun_slowa_stop(text: str) -> list:
    stop_words = stopwords.words("english")
    return [w for w in text if not w.lower() in stop_words]


def oczyszczanie_tekstu(text: str) -> str:
    emoticons = re.findall(r'[:|;][-]?[)|(|<>]', text)
    tekst_male_litery = text.lower()
    tekst_usuwanie_liczb = re.sub(r'\d', '', tekst_male_litery)
    tekst_usuwanie_html = re.sub(r'<.*?>', '', tekst_usuwanie_liczb)
    tekst_bez_znakow_przecinkowych = re.sub(r'\W(?<!\s)', '', tekst_usuwanie_html)
    tekst_bez_przestrzeni= tekst_bez_znakow_przecinkowych.strip()
    text_done = tekst_bez_przestrzeni + ' '.join(emoticons)
    return text_done


def stemming(word: str) -> str:
    ps = PorterStemmer()
    return ps.stem(word)


def tekst_tokenizer(text: str) -> list:
    cleaned = oczyszczanie_tekstu(text)
    tokens = word_tokenize(cleaned)
    without_stopwords = usun_slowa_stop(tokens)

    return [stemming(w) for w in without_stopwords if len(w) > 3]


def dodac_etykiety(x, y):
    for i in range(1, len(x) + 1):
        plt.text(i, y[i - 1], y[i - 1], ha="center", va="bottom")


def generowanie_danych() -> pd.DataFrame:
    """

    :rtype: object
    """
    df = pd.read_csv('tweets_airline.csv', sep=',',
                     usecols=['text', 'airline_sentiment'], encoding='utf-8')
    return df


def generowanie_plots(df: pd.DataFrame):
    ratings = df['airline_sentiment'].value_counts().sort_index()
    plt.bar(ratings.index, ratings.values)
    plt.title(f"Dystrybucja ocen recenzji")
    plt.xlabel("Opinia o ocenie informacji zwrotnej")
    plt.ylabel("Liczba recenzji")
    plt.show()

    sentiments = df['airline_sentiment'].value_counts()
    plt.pie(sentiments.values, shadow=True, labels=["Negatywne", "Neutralne", "Pozytywne"],
            startangle=90, autopct='%1.1f%%',
            colors=["Yellow", "Purple", "Green"])
    plt.title("Dystrybucja negatywnych, neutralnych i pozytywnych recenzji linii lotniczych")
    plt.show()


def wygeneruj_wordclouds(df: pd.DataFrame):
    stop_list = set(stopwords.words('english'))
    text_general = " ".join(review for review in df.text.astype(str))
    text_general = oczyszczanie_tekstu(text_general)
    wc = WordCloud(width=2500, height=2500, stopwords=stop_list, background_color='black', colormap='Paired')
    wc.generate(text_general)
    wc.to_file('wordclouds/wc_general.png')


def pokaz_wordclouds():
    for path in globe('wordclouds/*'):
        plt.imshow(matplotlib.image.imread(path))
        plt.title(path.split('\\')[1])
        plt.axis("off")
        plt.show()
