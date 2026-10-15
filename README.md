# Analiza sprzedaży

Projekt wykonany w ramach laboratorium z eksploracji danych.

## Opis danych
Zbiór danych (`data/sprzedaz.csv`) zawiera informacje o fikcyjnych zamówieniach: identyfikator transakcji (`id`), kanał sprzedaży (`kanal`), segment klienta (`segment`) oraz wartość zamówienia w złotych (`wartosc`).

## Wykonane analizy
* Weryfikacja struktury zbioru, spójności typów danych, braków wartości oraz duplikatów.
* Czyszczenie i standaryzacja danych tekstowych w kolumnie `kanal` (usunięcie zbędnych odstępów, zamiana na małe litery).
* Obliczenie kluczowych miar statystycznych (liczba zamówień, łączna suma sprzedaży, średnia wartość koszyka oraz mediana).
* Prezentacja sumy sprzedaży w podziale na kanały w postaci wykresu słupkowego.

## Technologie
Python, pandas, Jupyter, Streamlit, pytest, GitHub, Render

## Instrukcja uruchomienia lokalnego
1. Aktywuj środowisko wirtualne:
   ```cmd
   .venv\Scripts\activate