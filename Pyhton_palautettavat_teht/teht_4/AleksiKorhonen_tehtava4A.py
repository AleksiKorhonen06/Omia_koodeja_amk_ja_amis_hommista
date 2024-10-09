#Tee ohjelmakoodi, joka kysyy käyttäjältä etu- ja sukunimen, tallentaen ne omiin muuttujiin.
#Tee ohjelmaan funktio "LuoKayttajatunnus", joka etu ja sukunimen perusteella generoi käyttäjätunnuksen henkilölle,
#yhdistäen etunimen ensimmäiset 3 kirjainta ja sukunimen 3 ensimmäistä kirjainta, jonka perään tulee 3 sattumanvaraista numeroa. 
#Huom. Käyttäjätunnuksen kaikki kirjaimet pienellä.
#Esimerkiksi: Joni Järvenpää --> jonjär302


from random import randrange

def LuoKayttajaTunnus(etunimi, sukunimi):
    random_num = randrange(100, 1000)
    
    tunnus = etunimi[:3].lower() + sukunimi[:3].lower() + str(random_num)
    
    return tunnus

etunimi = input("Anna etunimesi: ")
sukunimi = input("Anna sukunimesi: ")

print("Käyttäjätunnuksesi on:", LuoKayttajaTunnus(etunimi, sukunimi))
