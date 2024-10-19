V1 = float(input("Paljonko sinulla on rahaa? "))
V2 = float(input("Paljonko pitsa maksaa? "))
V3 = V1 - V2


if V1 < V2:
    print("Rahasi eivät riitä pitsaan.")

else:
    print("Rahaa jäi ", V3)
    print("Nauti pitsasta!")