import streamlit as st
import pandas as pd
from analiza import (
    wczytaj_dane,
    wyczysc_dane,
    podsumowanie,
    sprzedaz_wg_kanalu,
)

st.set_page_config(
    page_title="Analiza sprzedazy",
    layout="wide",
)

st.title("Analiza sprzedaży projekt laboratoryjny")

df = wczytaj_dane("data/sprzedaz.csv")
df = wyczysc_dane(df)

st.sidebar.header("Filtry")

kanaly = sorted(df["kanal"].dropna().unique())

wybrane = st.sidebar.multiselect(
    "Kanal sprzedazy",
    kanaly,
    default=kanaly,
)

df_filtr = df[df["kanal"].isin(wybrane)]

wyniki = podsumowanie(df_filtr)

c1, c2, c3 = st.columns(3)

c1.metric(
    "Liczba zamowien",
    wyniki["liczba"],
)
c2.metric(
    "Suma sprzedazy",
    f'{wyniki["suma"]:.2f} zl',
)
c3.metric(
    "Srednia wartosc",
    f'{wyniki["srednia"]:.2f} zl',
)

st.subheader("Sprzedaz wedlug kanalu")

tabela = sprzedaz_wg_kanalu(df_filtr)
st.dataframe(tabela)

if not tabela.empty:
    st.bar_chart(
        tabela.set_index("kanal")["suma_sprzedazy"]
    )

st.subheader("Dane po filtrowaniu")
st.dataframe(df_filtr)

csv = df_filtr.to_csv(index=False).encode("utf-8")

st.download_button(
    "Pobierz CSV",
    csv,
    "wyniki.csv",
    "text/csv",
)