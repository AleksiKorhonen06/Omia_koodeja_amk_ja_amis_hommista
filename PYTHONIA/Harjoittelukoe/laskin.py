luku1 = int(input("anna luku: "))
luku2 = int(input("anna toka luku: "))
laskija = str(input("Millä luku lasketaan: "))

if laskija == "+":
    print (luku1 + luku2)
elif laskija == "-":
    print (luku1 - luku2)
elif laskija == "*":
    print (luku1 * luku2)
else:
    print("VÄÄRÄ MERKKI")