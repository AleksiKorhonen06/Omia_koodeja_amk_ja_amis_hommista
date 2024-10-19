nimi_list = []

while True:
    nimi = input("anna nimi: ")
    if nimi == '':
        break
    nimi_list.append(nimi)

nimi_list.sort()

print("Nimet allekkain:")
for nimi in nimi_list:
    print(nimi)