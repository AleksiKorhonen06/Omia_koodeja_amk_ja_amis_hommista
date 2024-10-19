lista = []
while True:
    nimi = input("anna nimesi: ")
    if nimi == "":
        break
    lista.append(nimi)
    
for nimi in lista:
    print(nimi)
