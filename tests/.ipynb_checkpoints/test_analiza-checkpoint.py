import pandas as pd
from analiza import wyczysc_dane, podsumowanie


def test_czyszczenie():
    df = pd.DataFrame({
        "kanal": [" Internet ", "SKLEP"],
        "wartosc": [100, 200]
    })
    wynik = wyczysc_dane(df)
    assert list(wynik["kanal"]) == ["internet", "sklep"]


def test_podsumowanie():
    df = pd.DataFrame({
        "wartosc": [100, 200, 300]
    })
    wynik = podsumowanie(df)
    assert wynik["liczba"] == 3
    assert wynik["suma"] == 600
    assert wynik["srednia"] == 200
    assert wynik["mediana"] == 200