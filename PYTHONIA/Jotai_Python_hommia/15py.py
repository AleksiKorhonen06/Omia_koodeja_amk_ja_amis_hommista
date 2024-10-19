nimet = []

while True:
    nimi = input("Anna etunimi: ")
    if nimi == "":
        break
    nimet.append(nimi)

print("Nimet listassa:")
for nimi in nimet:
    print(nimi)
