ostoslista = []

while True:
    tuote = input("Lisää tuote ostoslistaan (kirjoita 'valmis' lopettaaksesi): ").lower()
    if tuote == "valmis":
        break
    ostoslista.append(tuote)

ostoslista.sort()

print("\nOstoslistasi aakkosjärjestyksessä:")
for tuote in ostoslista:
    print(tuote)
