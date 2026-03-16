def wyszukiwanie_binarne(tablica, szukany_indeks):
    kroki = 0
    lewy = 0
    prawy = len(tablica) - 1

    while lewy <= prawy:
        kroki += 1
        srodk = (lewy + prawy) // 2

        print(f"Krok {kroki}: lewy={lewy}, prawy={prawy}, srodk={srodk}")

        if srodk == szukany_indeks:
            return kroki
        elif srodk < szukany_indeks:
            lewy = srodk + 1
        else:
            prawy = srodk - 1

    return kroki


# Testy dla wszystkich indeksów z tabeli
indeksy = [8, 17, 18, 22, 30, 45, 50, 56, 65, 70, 75, 80, 85]
wyniki = {}

for idx in indeksy:
    tablica = list(range(100))  # tablica 0..99
    kroki = wyszukiwanie_binarne(tablica, idx)
    wyniki[idx] = kroki
    print(f"Indeks {idx}: {kroki} kroków\\n")

print("Wyniki:", wyniki)
