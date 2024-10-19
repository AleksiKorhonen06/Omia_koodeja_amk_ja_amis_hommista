sana = [
"Vanni",

"Visanti",

"Rantasalo",

"Wuorimaa",

"Kilpi",

"Jalas",

"Kaira",

"Poijärvi",

"Linnala",

"Koskenniemi",

"Arni",

"Hainari",

"Pohjanpalo",

"Jännes",

"Kuusi",

"Talas",

"Rautapää",

"Aura",

"Wiherheimo",

"Kuusisto",

"Rantakari",

"Pinomaa",

"Paasilinna",

"Pihkala",

"Halsti",

"Kallia",

"Haarla",

"Harva",

"Heikinheimo",

"Päivänsalo",

"Helanen",

"Hattara",

"Helismaa"
]

list2 = []
print("Sanat, jotka alkavat antamallasi kirjaimella:")
for kirjain in sana:
    if kirjain[2] == "n":
        list2.append(kirjain)
        print(kirjain)

