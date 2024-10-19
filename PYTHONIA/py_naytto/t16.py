lista = []
while True:
    nimi = input("anna nimesi: ")
    if nimi == "":
        break
    lista.append(nimi)
lista.sort()

for nimi in lista:
    print(nimi)
