#Laajenna ohjelmaa siten, että se tulostaa syötettyjen lukujen keskiarvon.
#Syötteen loppumisesta kertovaa nollaa ei tule ottaa huomioon keskiarvon laskemisessa.
#Voit olettaa, että käyttäjä syöttää aina vähintään yhden luvun.

lukuM = 0
lukuS = 0
while True:
    luku = int(input("anna kokonaisluku: "))
    if luku == 0:
        print("lukujen lukumäärä oli: ", lukuS)
        print(KArvo)
        break
    elif luku == '':
        break
    else:
        lukuS += luku
        lukuM += 1
        KArvo = lukuS / lukuM