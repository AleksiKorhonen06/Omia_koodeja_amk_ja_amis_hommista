#- Harjoitella tekstin analysointia ja dictionary -rakennetta
#Läpipääsyssä huomioitavaa
#- Dictionary on pakollinen
#Tehtävä:
#Tee ohjelmisto, joka ottaa tekstiä syötteenä tallentaen sen muuttujaan.
#Tämän jälkeen ohjelmisto laskee 5 siinä eniten esiintyvää merkkiä. Tämä tieto varastoidaan dictionary -rakenteeseen. 
#Esimerkiksi tämä lause: 
#The Desmosedici Stradale was developed to combine racing performance with all the necessities for road use.
# he engine has a larger displacement than the MotoGP, 1,103 cm3 to be precise,
# to maximize the mid-range torque qualities that are so important for the bike's enjoyability on roads open to traffic, and to obtain torque and power at lower revs.
#Tuottaisi dictionaryn, jonka rakenne olisi { e: 39, t: 26, o: 25, a: 25, i: 21 }




from collections import Counter
text = "The Desmosedici Stradale was developed to combine racing performance with all the necessities for road use. he engine has a larger displacement than the MotoGP, 1,103 cm3 to be precise, to maximize the mid-range torque qualities that are so important for the bike's enjoyability on roads open to traffic, and to obtain torque and power at lower revs."
 
montako = {}
 
for kirjain in text:
    if kirjain == " ":
        continue  
    montako[kirjain] = montako.get(kirjain, 0) + 1
 
n = 5  # number of top values
 
counter = Counter(montako)
result = dict(counter.most_common(n))

#printing result
print ("Top 5 kirjainta olivat :\n "+ str(result))