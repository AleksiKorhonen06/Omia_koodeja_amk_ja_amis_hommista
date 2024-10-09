import re  # Tarvitaan erikoismerkkien tarkistamiseen

def TarkistaSalasana(salasana):
    if len(salasana) <= 8:
        return "Salasanan täytyy olla yli 8 merkkiä pitkä."

    if not any(kirjain.islower() for kirjain in salasana):
        return "Salasanassa täytyy olla vähintään yksi pieni kirjain."
    
    if not any(kirjain.isupper() for kirjain in salasana):
        return "Salasanassa täytyy olla vähintään yksi iso kirjain."
    
    if not any(kirjain.isnumeric() for kirjain in salasana):
        return "Salasanassa täytyy olla vähintään yksi numero."
    
    # Tarkista, että salasanassa on erikoismerkkejä
    if not re.search(r'[\W_]', salasana):  # \W tarkoittaa ei-aakkosnumeraalista, eli erikoismerkkiä
        return "Salasanassa täytyy olla vähintään yksi erikoismerkki."

    return "Salasana on hyväksytty!"


# Pyydetään käyttäjää syöttämään salasana
salasana = input("Anna salasana: ")

# Tulostetaan funktiosta saatu palaute
print(TarkistaSalasana(salasana))
