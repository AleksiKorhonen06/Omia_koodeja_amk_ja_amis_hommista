lista = ["Rikonen","Ruotsalainen","Huhtamäki","Männistö","Tapani","Mäkinen"]

kir = input("anna iso kirjain: ")
list2 = []
print("Sanat, jotka alkavat antamallasi kirjaimella:")
for kirjain in lista:
    if kirjain[0] == kir:
        list2.append(kirjain)
        print(kirjain)

