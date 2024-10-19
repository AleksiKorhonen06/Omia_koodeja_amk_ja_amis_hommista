lista = []
index = 0
while True:
    num = int(input("anna lukuja 1-9 välillä "))
    if num > 9:
        print("VIRHE")
        break
    if num == 0:
        break
    index += 1
    lista.append(num + index)
    num += index

for num in lista:
    print(num)
    
