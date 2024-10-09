#Tee sekunttikello, hyödyntäen time- ja datetime -kirjastoja.
#1. Hae tämän hetken aikaleima  datetime.now() -metodia.
#2. Erota muuttujiin tunnit, minuutit ja sekunnit.
#3. Tee ohjelmistoon tarvittavat toiminnot, jotka päivittävät sekunteja, minuutteja ja tunteja.
# Saat ohjelmistosi pysähtymään time.sleep(1) -metodilla
#4. Mieti eri tapoja, miten tämän toiminnon pystyy toteuttamaan?

import datetime
import time

def KelloNyt():
    aika = datetime.datetime.now()
    
    tunnit = aika.hour
    minuutit = aika.minute
    sekunnit = aika.second
    
    return f"{tunnit:02}:{minuutit:02}:{sekunnit:02}"

# Sekuntikellon toiminta
def sekuntikello():
    while True:
        print(KelloNyt(), end="\r")  
        time.sleep(1)

sekuntikello()
