#ad.1a

import re

#Usuwanie liczb


def delete_numbers(tekst: str) -> str:
    wynik = re.sub(r'\d', '', tekst)
    return wynik


#Usuwanie znaczników HTML


def delete_html(tekst: str) -> str:
    wynik = re.sub(r'<.*?>', '', tekst)
    return wynik


#FUsuwanie znaków interpunkcyjnych

def delete_punctuation(tekst: str) -> str:
    wynik = re.sub(r'\W(?<!\s)', '', tekst)
    return wynik