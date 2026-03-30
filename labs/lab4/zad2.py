# Zadanie 2
def czy_poprawne_nawiasy(wyrazenie):
    stos = []
    for znak in wyrazenie:
        if znak == '(':
            stos.append(znak)
        elif znak == ')':
            if not stos:
                return False
            stos.pop()
    return len(stos) == 0

wyrazenie = input("Podaj wyrażenie z nawiasami: ")
if czy_poprawne_nawiasy(wyrazenie):
    print("Nawiasy są poprawnie zagnieżdżone.")
else:
    print("Nawiasy są niepoprawne.")