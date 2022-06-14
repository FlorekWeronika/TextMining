import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer


def pozytywny_odbior(df: pd.DataFrame):
    df_pos = df[df['airline_sentiment'] == "positive"]
    vectorizer = TfidfVectorizer(tokenizer=text_tokenizer)
    x_transform_pos = vectorizer.fit_transform(df_pos['text'])
    column_names_pos = vectorizer.get_feature_names_out()
    array_pos = x_transform_pos.toarray()
    token_column_sums_pos = np.sum(array_pos, axis=0)
    highest_weight_indexes_pos = np.argpartition(token_column_sums_pos, -10)[-10:]
    highest_weight_token_names_pos = []
    highest_weight_pos = []

    for index in np.nditer(highest_weight_indexes_pos):
        highest_weight_token_names_pos.append((column_names_pos[index]))
        highest_weight_pos.append(token_column_sums_pos[index])

    data_pos = {'Tokens': highest_weight_token_names_pos, 'Weights': highest_weight_pos}
    tokens_pos = pd.DataFrame(data_pos)
    sorted_tokens = tokens_pos.sort_values(by=['Weights'], ascending=True)
    print("\n 10 najważniejszych tokenów za pozytywne recenzje")
    print(tabulate(sorted_tokens, headers='keys', tablefmt='psql'))
    plt.bar(sorted_tokens['Tokens'], sorted_tokens['Weights'])
    plt.xlabel("Tokens")
    plt.ylabel("Weights")
    plt.xticks(rotation=25)
    plt.gcf().subplots_adjust(bottom=0.30)
    plt.title("10 najważniejszych tokenów za pozytywne recenzje")
    plt.show()
