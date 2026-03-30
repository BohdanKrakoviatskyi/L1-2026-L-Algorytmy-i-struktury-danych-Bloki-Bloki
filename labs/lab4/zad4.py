# Zadanie 4
def oblicz_onp(wyrazenie):
    stos = []
    tokeny = wyrazenie.split()

    for token in tokeny:
        if token.lstrip('-').isdigit():
            stos.append(int(token))
        elif token in ['+', '-', '*', '/', '^']:
            if len(stos) < 2:
                return "Błąd: za mało argumentów."

            b = stos.pop()
            a = stos.pop()

            if token == '+':
                stos.append(a + b)
            elif token == '-':
                stos.append(a - b)
            elif token == '*':
                stos.append(a * b)
            elif token == '/':
                if b == 0:
                    return "Błąd: dzielenie przez zero."
                stos.append(a / b)
            elif token == '^':
                stos.append(a ** b)
        elif token == '=':
            if len(stos) == 1:
                return stos.pop()
            return "Błąd: niepoprawne wyrażenie."
        else:
            return f"Błąd: nieznany token {token}"

    return "Błąd: brak znaku '=' na końcu."

wyrazenie = input("Podaj wyrażenie w ONP: ")
wynik = oblicz_onp(wyrazenie)
print("Wynik:", wynik)