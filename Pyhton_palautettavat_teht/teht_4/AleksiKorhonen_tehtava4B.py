#Ylläolevan superturvallisen näppäinlukon salasana koostuu mitä todennäköisimmiten numeroista 1, 7, 9 ja 0.
# Tiedustelun mukaan salasanan pituus on 6 merkkiä.
#Tehtävänäsi on tehdä ohjelmistokoodi, joka tulostaa jokaisen eri vaihtoehdon kyseisillä merkeillä.
#Hyödynnä ratkaisussa rekursiivista funktiorakennetta.


tries = 0

def luo_vaihtoehdot(nykyinen, salasanan_Pituus, tries):
    if salasanan_Pituus == 0:
        print(nykyinen)
        return tries + 1

    for vaihtoehdot in ['1', '7', '9', '0']:
        tries = luo_vaihtoehdot(nykyinen + vaihtoehdot, salasanan_Pituus - 1, tries)

    return tries

tries = luo_vaihtoehdot("", 6, tries)
print("Yhteensä yrityksiä:", tries)