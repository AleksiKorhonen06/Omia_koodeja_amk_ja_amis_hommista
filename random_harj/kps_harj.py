import secrets

ai_valinta = secrets.choice(["kivi", "paperi", "sakset"])

pelaaja_valinta = input("Valitse kivi, paperi tai sakset: ").lower()

if pelaaja_valinta not in ["kivi", "paperi", "sakset"]:
    print("Virheellinen valinta! Yritä uudelleen.")
else:
    print(f"AI valitsi: {ai_valinta}")
    
    if pelaaja_valinta == ai_valinta:
        print("Tasapeli!")
    elif (pelaaja_valinta == "kivi" and ai_valinta == "sakset") or \
        (pelaaja_valinta == "paperi" and ai_valinta == "kivi") or \
        (pelaaja_valinta == "sakset" and ai_valinta == "paperi"):
        print("Voitit!")
    else:
        print("AI voitti!")
