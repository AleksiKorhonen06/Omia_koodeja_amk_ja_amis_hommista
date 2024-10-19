while True:
    pituus = int(input("anna pituus: "))
    if pituus > 0:
        break
    
while True:
    hinta = float(input("anna hinta: "))
    if hinta > 0:
        break
    
if pituus > 50:
    print(pituus * 1.25 * hinta)
else:
    print(pituus * 1.50 * hinta)
    