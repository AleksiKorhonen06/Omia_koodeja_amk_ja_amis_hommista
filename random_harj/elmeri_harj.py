while True:
    try:
        data1 = float(input("Anna numero (data1): "))
        break
    except ValueError:
        print("Anna numero pälli")

while True:
    try:
        data2 = float(input("Anna numero (data2): "))
        break 
    except ValueError:
        print("Anna numero pälli")

print(f"Hyvä! Numerot ovat: {data1} ja {data2}")
