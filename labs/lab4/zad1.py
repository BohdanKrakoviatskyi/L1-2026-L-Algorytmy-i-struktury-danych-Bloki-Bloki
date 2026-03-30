stos = []

liczby = input("Podaj liczby oddzielone spacjami: ").split()

for x in liczby:
    stos.append(x)

print("Odwrotna kolejność:")
while len(stos) > 0:
    print(stos.pop(), end=" ")