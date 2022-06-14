from pozytywny_odbior import pozytywny_odbior
from negatywny_odbior import negatywny_odbior
from opinia import opinia
from utilitis import *

def main():
    df = generowanie_danych()
    generowanie_plots(df)
    wygeneruj_wordclouds(df)
    pokaz_wordclouds()
    pozytywny_odbior(df)
    negatywny_odbior(df)
    opinia(df)


if __name__ == "__main__":
    main()