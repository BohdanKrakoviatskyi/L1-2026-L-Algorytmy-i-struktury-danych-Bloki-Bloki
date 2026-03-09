def czy_palindrom_rek(s):
    # usuwamy spacje i zmieniamy na małe litery
    s = s.replace(" ", "").lower()

    # przypadki bazowe
    if len(s) <= 1:
        return True

    # pierwszy != ostatni → NIE palindrom
    if s[0] != s[-1]:
        return False

    # rekurencyjnie sprawdzamy środek
    srodek = s[1:-1]
    return czy_palindrom_rek(srodek)


# testy z zadania:
print(czy_palindrom_rek("radar"))  # True
print(czy_palindrom_rek("Anna"))  # True  (a n n a)
print(czy_palindrom_rek("kayak"))  # True
print(czy_palindrom_rek("Python"))  # False  (p y t h o n)
