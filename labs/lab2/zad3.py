def dokladnie_dwa_duplikaty(L):
    # liczymy wystąpienia każdego elementu
    from collections import Counter
    licznik = Counter(L)

    # sprawdzamy czy dokładnie jeden element ma licznik=2, reszta=1
    duplikaty = sum(1 for count in licznik.values() if count == 2)
    return duplikaty == 1 and all(count == 1 for count in licznik.values() if count != 2)


# przykładowe testy z tabeli:
print(dokladnie_dwa_duplikaty([1]))  # False (za mało elementów)
print(dokladnie_dwa_duplikaty([1, 2]))  # False (brak duplikatów)
print(dokladnie_dwa_duplikaty([1, 1]))  # True
print(dokladnie_dwa_duplikaty([1, 2, 3]))  # False
print(dokladnie_dwa_duplikaty([4, 1, 4]))  # True
print(dokladnie_dwa_duplikaty([5, 6, 5]))  # True
print(dokladnie_dwa_duplikaty([7, 8, 7, 9]))  # False (więcej niż 2 sevens? Wait, [7,8,7,9] ma jeden duplikat 7)
# itd. zgodnie z tabelą
