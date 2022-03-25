#Wyodrębnienie emotikonów z tekstu

import re

def emotikony(tekst: str) -> list:
    wynik = re.findall(r'[:|;][-]?[)|(|<|>]', tekst)
    return wynik