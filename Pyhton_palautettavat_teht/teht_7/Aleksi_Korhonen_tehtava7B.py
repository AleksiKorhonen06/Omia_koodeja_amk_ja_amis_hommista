#Läpipääsyssä huomioitavaa
#- Tee toiminnot käyttämällä for -silmukkarakennetta
#- splice rakenteiden käyttön on kielletty, kuten [::-1]

#Tehtävä:
#Tee ohjelmisto, joka kysyy käyttäjältä sanaa.
#tämän jälkeen aseta teksti toiseen muuttujaan, kääntäen tekstin "väärinpäin".
#Käännä myös isot kirjaimet pieniksi

#Esimerkki:
#Teksti: Tunturi
#Käännettynä: IRUTNUt

sana = input("Anna jokin sana: ")

vaarinpain_sana = []
sanan_pituus = len(sana)

while sanan_pituus > 0:
    vaarinpain_sana.append(sana[sanan_pituus - 1])
    sanan_pituus -= 1

print(f"Sanasi väärinpäin on: {vaarinpain_sana}")
