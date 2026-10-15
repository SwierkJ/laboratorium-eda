import pandas as pd


def wczytaj_dane(sciezka):
    """Wczytuje dane z pliku CSV o zadanym separatorze."""
    return pd.read_csv(sciezka, sep=";")


def wyczysc_dane(df):
    """Tworzy kopię i ujednolica zapis w kolumnie 'kanal'."""
    wynik = df.copy()
    wynik["kanal"] = wynik["kanal"].astype(str).str.strip().str.lower()
    return wynik


def podsumowanie(df):
    """Zwraca słownik z podstawowymi statystykami wartości zamówień."""
    return {
        "liczba": int(len(df)),
        "suma": float(df["wartosc"].sum()) if not df.empty else 0.0,
        "srednia": float(df["wartosc"].mean()) if not df.empty else 0.0,
        "mediana": float(df["wartosc"].median()) if not df.empty else 0.0,
    }


def sprzedaz_wg_kanalu(df):
    """Zwraca DataFrame z sumą sprzedaży w podziale na kanały."""
    if df.empty:
        return pd.DataFrame(columns=["kanal", "suma_sprzedazy"])
    return (
        df.groupby("kanal", as_index=False)["wartosc"]
        .sum()
        .rename(columns={"wartosc": "suma_sprzedazy"})
    )