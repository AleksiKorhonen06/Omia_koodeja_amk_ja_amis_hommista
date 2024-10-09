print("\n vastaa vain 1 tai 2")
print("1 = pakene")
print("2 = Lyö opettajaa\n")
ans = int(input(" Olet Oppilaana luokassa, joka on täynnä oppilaita. Ope kysyy kysymyksen, johon et tiedä vastausta. Mitä teet?: "))

if ans == 1:
    print("\n 1 = Vastaat rehellisesti pakeneesi luokasta")
    print("\n Juokset karkuun")
    ans2 = int(input("Pakenit ikkunasta. Olet nyt ulkona. ope kävelee parkkipaikalla vastaan, ja kysyy Eikös sinun pitäisi olla tunnilla opettamassa? Mitä teet?"))
    if ans2 == 1:
        print("Peli ohi GG")
    if ans2 == 2:
        print("Juoksit karkuun, etkä palannut enää koululle. Huomaat seuraavana aamuna, että avainlätkäsi ei avaa enää koulun ovia. Hävisit pelin.")

if ans == 2: 
    print("1 = luovutat ja hyväksyt tappiosi")
    print("2 = Kutsut Alexander Stubin apuusi")
    ans2 = int(input("löit opettajaa, mutta ope oli liian iso levu ja sun damage ei riitä mitä teet seuraavaksi"))
    if ans2 == 1:
        print("Hävisit pelin BG")
    if ans2 == 2:
        print("Alexander Stub köpelöi sinua (Bad ending)")