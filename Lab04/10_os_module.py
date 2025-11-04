import os

sciezka_bazowa = os.path.join(os.getcwd(), 'testy_os')

# 1. Tworzenie katalogów
os.makedirs(sciezka_bazowa, exist_ok=True) # exist_ok=True zapobiega błędowi, jeśli już istnieje
print(f"Aktualny katalog roboczy: {os.getcwd()}")

# 2. Tworzenie pliku (symulacja)
sciezka_pliku = os.path.join(sciezka_bazowa, 'dane.txt')
with open(sciezka_pliku, 'w') as f:
    f.write("Testowe dane.")

# 3. Sprawdzenie istnienia
if os.path.exists(sciezka_pliku):
    print(f"Plik istnieje: {os.path.isfile(sciezka_pliku)}")

# 4. Lista zawartości
zawartosc = os.listdir(sciezka_bazowa)
print(f"Zawartość folderu: {zawartosc}")

# 5. Sprzątanie (usunięcie pliku i katalogu)
os.remove(sciezka_pliku)
os.rmdir(sciezka_bazowa)

