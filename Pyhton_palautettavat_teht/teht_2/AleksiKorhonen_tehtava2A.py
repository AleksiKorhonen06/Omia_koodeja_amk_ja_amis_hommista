while True:
    try:
        luku1 = float(input("Anna numero1: "))
        break
    except ValueError:
        print("Anna numero pälli")

while True:
    try:
        luku2 = float(input("Anna numero2: "))
        break 
    except ValueError:
        print("Anna numero pälli")
        

while True:
    try:
        laskin = input("anna merkki millä haluat laskea sen (+ - * /): ")
        if laskin != "+" or "-" or "*" or "/":
            break
    except:
        print("anna jokin laskutoimitus")

if laskin == "+":
    print(f"{luku1 + luku2}")
    
elif laskin == "-":
    print(f"{luku1 - luku2}")
    
elif laskin == "*":
    print(f"{luku1 * luku2}")
    
elif laskin == "/":
    print(f"{luku1 / luku2}")

else:
    print("virhe")