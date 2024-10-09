#Läpipääsyssä huomioitavaa
#- Muista viantarkastelu
#Tehtävä:
#Tee ohjelmisto, joka kysyy käyttäjältä kahta lukua: ensimmäisen luvun tulee olla pienempi kuin toisen luvun.
#Laske, montako prosenttia ensimmäinen luku on toisesta luvusta.
#Tämän jälkeen visualisoi prosenttiluku "latauspalkkimaisesti".
#esimerkiksi.
#Luku 1: 80
#Luku 2: 200
#=> luku 80 on 40% luvusta 200
#40% 
#| ⚫⚫⚫⚫⚫⚫⚫⚫⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪ |



num1 = float(input("\nAnna ensimmäinen numero (pienempi): "))
num2 = float(input("Anna toinen numero (suurempi): "))


if num1 < num2:
    prosentti = (num1 / num2) * 100
    print(f"Luku {num1} on {prosentti:.2f}% luvusta {num2}")
    
    palkin_pituus = 25
    palkki = int((prosentti / 100) * palkin_pituus)
    
    palkki_visuaalisesti = "⚫" * palkki + "⚪" * (palkin_pituus - palkki)
    print(f"latausbaari: {palkki_visuaalisesti}")
else:
    print("Virhe: Ensimmäisen luvun pitää olla pienempi kuin toisen.")
