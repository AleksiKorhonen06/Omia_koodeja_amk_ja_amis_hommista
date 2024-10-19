#Tee ohjelma, joka pyytää käyttäjää syöttämään kokonaislukuja. Ohjelma pyytää lukuja niin kauan kunnes käyttäjä syöttää nollan. 
#Osa 1: lukumäärä
#Syötteiden lukemisen jälkeen ohjelman tulee tulostaa syötettyjen lukujen lukumäärä. Syötteen loppumisesta kertovaa nollaa ei tule ottaa huomioon lukumäärässä. 
#Tarvitset tässä uuden muuttujan, jonka avulla pidät kirjaa luettujen lukujen määrästä. 
lukuM = 0

while True:
    luku = int(input("anna kokonaisluku: "))
    if luku == 0:
        print("Ei sitten.")
        print("lukujen lukumäärä oli: ", lukuM)
        break
    else:
        lukuM += 1
