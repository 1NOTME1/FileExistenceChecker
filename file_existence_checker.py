import os

def sprawdz_sciezki(nazwa_pliku_txt, wynikowy_plik_txt="nieistniejace_sciezki.txt"):
    with open(nazwa_pliku_txt, 'r', encoding='utf-8') as plik:
        sciezki = plik.readlines()

    nieistniejace = []

    for sciezka in sciezki:
        sciezka = sciezka.strip()  
        if os.path.exists(sciezka):
            print(f"Ścieżka istnieje: {sciezka}")
        else:
            print(f"Ścieżka NIE istnieje: {sciezka}")
            nieistniejace.append(sciezka)

    with open(wynikowy_plik_txt, 'w', encoding='utf-8') as plik_wynikowy:
        for sciezka in nieistniejace:
            plik_wynikowy.write(sciezka + "\n")

nazwa_pliku = "sciezki.txt"
sprawdz_sciezki(nazwa_pliku)

