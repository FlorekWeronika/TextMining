import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

def opinia(df: pd.DataFrame):
    x = df['text']
    y = df['airline_sentiment']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)
    vectorizer = CountVectorizer(tokenizer=text_tokenizer)
    x_transform_train = vectorizer.fit_transform(x_train)
    x_transform_test = vectorizer.transform(x_test)
    dt = DecisionTreeClassifier()
    dt.fit(x_transform_train, y_train)
    dt_score = dt.score(x_transform_test, y_test)
    print(f"Dokładność przewidywania modelu drzewa decyzyjnego - {dt_score * 100} %.")
    y_pred_dt = dt.predict(x_transform_test)
    print("Raport klasyfikacyjny Drzewa Decyzyjnego")
    print(classification_report(y_test, y_pred_dt))

    svml = svm.SVC()
    svml = svml.fit(x_transform_train, y_train)
    svml_score = svml.score(x_transform_test, y_test)
    print(f"Obsługa dokładności przewidywania modelu maszyny wektorowej - {svml_score * 100} %.")
    y_pred_svml = svml.predict(x_transform_test)
    print("Raport klasyfikacji dla maszyny wektorów nośnych")
    print(classification_report(y_test, y_pred_svml))

    rfcl = RandomForestClassifier(n_estimators=150)
    rfcl = rfcl.fit(x_transform_train, y_train)
    rfcl_score = rfcl.score(x_transform_test, y_test)
    print(f"Dokładność przewidywania losowego klasyfikatora lasu = {rfcl_score * 100} %.")
    y_pred_rfcl = rfcl.predict(x_transform_test)
    print("Raport klasyfikacyjny dla losowego klasyfikatora leśnego")
    print(classification_report(y_test, y_pred_rfcl))

