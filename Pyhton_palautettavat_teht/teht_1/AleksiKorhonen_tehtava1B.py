kkTulot = float(input("\nMitkä ovat keskimääräiset kuukausi tulosi: "))
RuokaHnt = float(input("Kuinka kallista on koulu ruokasi (yksi ateria): "))
PaivienMaaraPerV = float(input("Kuinka monta kertaa käyt syömässä koulussa yhden viikon aikana: "))
MuutMenot = float(input("Kuinka suuret ovat muut kulusi, kuten vuokra: "))

vuosiTulosi = kkTulot * 12  
kouluruokaKuukausi = RuokaHnt * PaivienMaaraPerV * 4  
kuukausiMenotYhteensa = kouluruokaKuukausi + MuutMenot  
jääRahaa = kkTulot - kuukausiMenotYhteensa  
säästöt4Vuotta = jääRahaa * 0.20 * 12 * 4  

print(f"\nVuositulosi ovat: {vuosiTulosi}")
print(f"Sinulla menee kouluruokaan kuukaudessa: {kouluruokaKuukausi}")
print(f"Kuukausimenosi yhteensä ovat: {kuukausiMenotYhteensa}")
print(f"Sinulle jää rahaa kaikkien menojen jälkeen: {jääRahaa}")
print(f"\nJos säästäisit 20 prosenttia kuukauden aikana 4 vuoden ajan, säästäisit: {säästöt4Vuotta}\n")
