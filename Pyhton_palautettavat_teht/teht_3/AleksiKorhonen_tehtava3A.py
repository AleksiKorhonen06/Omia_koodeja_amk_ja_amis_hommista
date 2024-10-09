minun_ika = 18
quess = int(input("arvaa ikäni: "))
while quess != minun_ika:
    quess = int(input("arvaa uudestaan: "))
    if quess == minun_ika:
        print("arvasit oikein")