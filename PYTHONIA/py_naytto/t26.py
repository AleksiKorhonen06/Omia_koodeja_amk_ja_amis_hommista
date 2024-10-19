
def keskimmainen_indeksi(lista):
    pienin = min(lista)
    suurin = max(lista)
    keskimmainen = sum(lista) - pienin - suurin

    return lista.index(keskimmainen)

lista = [7, 15, 3]
print(lista)
print("keskimmäisen indexi on", keskimmainen_indeksi(lista))


