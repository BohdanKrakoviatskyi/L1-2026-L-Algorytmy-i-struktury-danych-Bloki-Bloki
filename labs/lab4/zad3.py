# Zadanie 3
stos_undo = []

while True:
    polecenie = input("Wpisz tekst, 'undo' albo 'exit': ")

    if polecenie.lower() == 'exit':
        print("Koniec programu.")
        break
    elif polecenie.lower() == 'undo':
        if stos_undo:
            usuniety = stos_undo.pop()
            print("Cofnięto:", usuniety)
        else:
            print("Brak operacji do cofnięcia.")
    else:
        stos_undo.append(polecenie)
        print("Dodano:", polecenie)

    print("Aktualny stos:", stos_undo)