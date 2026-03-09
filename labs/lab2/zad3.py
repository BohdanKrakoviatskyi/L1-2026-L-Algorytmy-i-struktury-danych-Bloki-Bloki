def funkcja_rekurencyjna(n):
    if n <= 2:
        return 2
    elif n == 3:
        return 3
    else:
        return funkcja_rekurencyjna(n - 1) + funkcja_rekurencyjna(n - 2)

# Obliczenia dla n od 1 do 15 (uzupełnienie tabeli)
wyniki = []
for i in range(1, 16):
    wyniki.append((i, funkcja_rekurencyjna(i)))
print(wyniki)
