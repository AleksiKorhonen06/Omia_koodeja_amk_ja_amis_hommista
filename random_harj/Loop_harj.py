import random
oikee_vastaus = random.randrange(1,10)

arv = int(input("arvaa oikea luku 1-10: "))

while arv != oikee_vastaus:
    print("VÄÄRIN VITUN PASKA")
    arv = int(input("arvaa UUDESTAAN: "))

    if arv == oikee_vastaus:
        print("OIKEN MENI")
        break