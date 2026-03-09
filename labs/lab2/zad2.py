def min_i_max(macierz):
    # spłaszczamy macierz do jednej listy
    wszystkie = [liczba for wiersz in macierz for liczba in wiersz]
    return (min(wszystkie), max(wszystkie))

# przykład z zadania
macierz = [
    [3, 2, 8, 1],
    [5, 9, 4, 7],
    [6, 1, 2, 5]
]
print(min_i_max(macierz))  # (1, 9)

#wynik
#MIN: 1 (wiersz 2, kolumna 2)
#MAX: 9 (wiersz 2, kolumna 1)