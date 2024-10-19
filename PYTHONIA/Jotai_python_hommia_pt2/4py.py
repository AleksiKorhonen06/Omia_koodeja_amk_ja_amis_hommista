sana = [
    "Vanni", "Visanti", "Rantasalo", "Wuorimaa", "Kilpi", "Jalas", "Kaira",
    "Poijärvi", "Linnala", "Koskenniemi", "Arni", "Hainari", "Pohjanpalo",
    "Jännes", "Kuusi", "Talas", "Rautapää", "Aura", "Wiherheimo", "Kuusisto",
    "Rantakari", "Pinomaa", "Paasilinna", "Pihkala", "Halsti", "Kallia",
    "Haarla", "Harva", "Heikinheimo", "Päivänsalo", "Helanen", "Hattara", "Helismaa"
]

list2 = []
alkukirjain = input("Anna kirjain: ")

print(f"Sanat, jotka alkavat kirjaimella '{alkukirjain}':")
for kirjain in sana:
    if kirjain.startswith(alkukirjain):
        list2.append(kirjain)

list2.sort()
for kirjain in list2:
    print(kirjain)
