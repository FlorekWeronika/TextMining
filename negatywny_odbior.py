import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from tabulate import tabulate

def negatywny_odbior(df: pd.DataFrame):
    df_neg = df[df['airline_sentiment'] == "negative"]
    vectorizer = TfidfVectorizer(tokenizer=text_tokenizer)
    x_transform_neg = vectorizer.fit_transform(df_neg['text'])
    column_names_neg = vectorizer.get_feature_names_out()
    array_neg = x_transform_neg.toarray()
    token_column_sums_neg = np.sum(array_neg, axis=0)
    highest_weight_indexes_neg = np.argpartition(token_column_sums_neg, -10)[-10:]
    highest_weight_token_names_neg = []
    highest_weight_neg = []

    for index in np.nditer(highest_weight_indexes_neg):
        highest_weight_token_names_neg.append((column_names_neg[index]))
        highest_weight_neg.append(token_column_sums_neg[index])

    data_neg = {'Tokens': highest_weight_token_names_neg, 'Weights': highest_weight_neg}
    tokens_neg = pd.DataFrame(data_neg)
    sorted_tokens = tokens_neg.sort_values(by=['Weights'], ascending=True)
    print("\n 10 najważniejszych tokenów za negatywne recenzje")
    print(tabulate(sorted_tokens, headers='keys', tablefmt='psql'))
    plt.bar(sorted_tokens['Tokens'], sorted_tokens['Weights'])
    plt.xlabel("Tokens")
    plt.ylabel("Weights")
    plt.xticks(rotation=25)
    plt.gcf().subplots_adjust(bottom=0.30)
    plt.title("10 najważniejszych tokenów za negatywne recenzje")
    plt.show()

