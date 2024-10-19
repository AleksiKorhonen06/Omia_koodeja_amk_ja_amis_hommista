#Laajenna ohjelmaa siten, että se tulostaa syötettyjen lukujen summa. Syötteen loppumisesta kertovaa nollaa ei tule ottaa huomioon summan laskemisessa. 
#Ohjelman tulostus laajenee seuraavasti: 

lukuM = 0

while True:
    luku = int(input("anna kokonaisluku: "))
    if luku == 0:
        print("Ei sitten.")
        print("lukujen lukumäärä oli: ", lukuM)
        break
    else:
        lukuM += luku
