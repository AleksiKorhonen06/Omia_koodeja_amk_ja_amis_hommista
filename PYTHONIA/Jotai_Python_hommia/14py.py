print("Anna kokonaislukuja, niin lasken")
sum = 0
while True:
    i = int(input("Anna luku: "))
    if i == 0:
        break
    
    sum += i

print("lukujen summa on", sum)