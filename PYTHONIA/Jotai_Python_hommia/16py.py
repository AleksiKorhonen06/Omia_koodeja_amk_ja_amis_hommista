sukunimet = ["Pekkala", "Suominen", "Pitkämäki", "Männikkö", "Tapanila", "Mäki"]

alkukirjain = input("Millä alkukirjaimella etsitään: ")

loytyneet_nimet = [nimi for nimi in sukunimet if nimi.startswith(alkukirjain)]

for nimi in loytyneet_nimet:
    print(nimi)
