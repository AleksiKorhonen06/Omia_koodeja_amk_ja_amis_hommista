lukuM = 0
summa = 0
while True:
    num = int(input("anna kokonais luku: "))
    lukuM += 1
    summa += num
    if num == 0:
        break
lukuM -= 1
print("lukujen lukumäärä on", lukuM)
print("luujen summa on", summa)

Kesk_arvo = summa / lukuM

print("lukujen keskiarvo on", Kesk_arvo)