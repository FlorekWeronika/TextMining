#Wyodrębnienie hasztagów z tekstu

import re

def hashtag (tekst: str) -> list:
    wynik = re.findall(r'#[a-z0-9_]+', tekst)
    return wynik