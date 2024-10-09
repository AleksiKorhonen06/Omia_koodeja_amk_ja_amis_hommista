# copyrighted by agentti & ape
# all rights reserved, jakaminen kiellettyä

from datetime import datetime

nyt = datetime.now()
joulu = datetime(nyt.year, 12, 24)
viimeJoulu = datetime(nyt.year - 1, 12, 24)

if nyt > joulu:
    joulu = datetime(nyt.year + 1, 12, 24)

def PaivaaJouluun():
    ero = joulu - nyt
    paiva_ero = ero.days
    return paiva_ero

def PaivatviimeJoulusta():
    ero = nyt - viimeJoulu
    paiva_ero = ero.days
    return paiva_ero

def Synttareista_jouluun():
    while True:
        try:
            synttari_paiva = int(input("Mikä päivä syntymäpäiväsi on? "))
            synttari_kuu = int(input("Mikä kuukausi syntymäpäiväsi on? "))
            
            synttärit = datetime(nyt.year, synttari_kuu, synttari_paiva)

            if synttärit > joulu:
                seuraava_joulu = datetime(nyt.year + 1, 12, 24)
            else:
                seuraava_joulu = joulu

            ero = seuraava_joulu - synttärit
            paiva_ero = ero.days
            return paiva_ero
        except ValueError:
            print("Virheellinen päivämäärä. Yritä uudelleen.")
        except Exception as e:
            print(f"Odottamaton virhe: {e}")

while True:
    try:
        valinta = int(input("Valitse 1: Kuinka monta päivää on jouluaattoon tästä hetkestä\n"
                            "Valitse 2: Kuinka monta päivää on jouluaattoon syntymäpäivästäsi\n"
                            "Anna valintasi (1 tai 2): "))
        
        if valinta == 1:
            print(f"Jouluaattoon on {PaivaaJouluun()} päivää tästä hetkestä.")
            print(f"Jouluaatosta on {PaivatviimeJoulusta()} päivää tästä hetkestä.")

            break
        elif valinta == 2:
            print(f"Jouluaattoon on {Synttareista_jouluun()} päivää syntymäpäivästäsi.")
            break
        else:
            print("Virheellinen valinta, yritä uudelleen.")
    except ValueError:
        print("Syötteen tulee olla numero (1 tai 2).")
