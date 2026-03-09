def druga_najwieksza(lista):
    # usuwamy duplikaty
    unikalne = list(set(lista))
    # sortujemy malejąco
    unikalne.sort(reverse=True)
    # druga największa to element o indeksie 1
    return unikalne[1]

# przykłady z zadania
print(druga_najwieksza([10, 20, 4, 45, 99, 99]))  # 45
print(druga_najwieksza([1, 2, 3, 4, 5]))          # 4
print(druga_najwieksza([10, 10, 10, 9]))          # 9
