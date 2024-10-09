

from random import randrange

random_numero = randrange(1, 6)
Voittavat_numerot = [1, 2, 4]
yrityksien_maara = 0

while True:
    arvatut_numerot = [randrange(1, 6) for _ in range(len(Voittavat_numerot))]

    print(f"Yritys {yrityksien_maara + 1}, arvatut numerot: {arvatut_numerot}")

    yrityksien_maara += 1

    if arvatut_numerot == Voittavat_numerot:
        print(f"Voittavat numerot olivat: {Voittavat_numerot}")
        print(f"Koodi yritti arvata voittavia numeroita {yrityksien_maara} kertaa")
        break

"""from random import randrange

random_numero = randrange(1, 99)
Voittavat_numerot = [13,13,24,44,11,12]
yrityksien_maara = 0
arvatut_numerot = []

while True:
    while len(arvatut_numerot) < len(Voittavat_numerot):
        arvatut_numerot.append(randrange(1, 99))

    print(f"Yritys {yrityksien_maara + 1}, arvatut numerot: {arvatut_numerot}")
    
    # Tarkistetaan jokainen arvaus ja päivitetään väärät numerot
    for arvaus in range(len(Voittavat_numerot)):
        if arvatut_numerot[arvaus] != Voittavat_numerot[arvaus]:
            arvatut_numerot[arvaus] = randrange(1, 99)

    yrityksien_maara += 1
    
    if arvatut_numerot == Voittavat_numerot:
        print(f"Voittavat numerot olivat: {Voittavat_numerot}")
        print(f"Koodi yritti arvata voittavia numeroita {yrityksien_maara} kertaa")
        break

"""