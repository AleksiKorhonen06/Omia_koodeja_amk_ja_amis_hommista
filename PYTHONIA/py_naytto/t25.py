def ajanTarkastus(a, b):

    if a > 24 or a < 0:
        return False
    if b > 60 or b < 0:
        return False
    
    else:
        return True
        
kello = ajanTarkastus(12, 30)
print(kello)