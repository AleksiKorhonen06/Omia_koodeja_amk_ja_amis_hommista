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

for index in range(len(sana) - 1, -1, -1):
    vaarinpain_sana.append(sana[index])

vaarinpain_sana = ''.join(vaarinpain_sana)
vaarinpain_sana = vaarinpain_sana.swapcase()

print(f"Sanasi väärinpäin ja kirjaimet vaihdettu on: {vaarinpain_sana}")
