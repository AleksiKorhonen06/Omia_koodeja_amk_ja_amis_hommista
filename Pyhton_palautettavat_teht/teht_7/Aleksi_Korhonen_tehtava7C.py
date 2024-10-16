
#Läpipääsyssä huomioitavaa

#- Ainostaan for -loop rakenne on sallittu sorttauksessa!
#- While sallittu numeroiden kysymisessä

#Tehtävä:
#Tee ohjelmisto, joka kysyy käyttäjältä numeroita ja asettaa niitä listaan. 
#Kun käyttäjä syöttää tyhjän syötteen, ohjelmisto järjestää käyttäjän syöttämät
#numerot järjestykseen uuteen listaan, pienimmästä suurimpaan käyttäen ainoastaan
#apunaan ainoastaan for -looppeja.




#järjestäminen
def jarjesta():
    for i in range(0, len(num_list)):
        for j in range(i+1, len(num_list)):
            if num_list[i] >= num_list[j]:
                num_list[i], num_list[j] = num_list[j],num_list[i]
    
    print("numerot pienimmästä suurimpaan", num_list)


kysy_num = int(input("anna jokin kokonais luku (kirjoita 0 lopettaaksesi): "))
num_list = []
while kysy_num != 0:
    num_list.append(kysy_num)
    kysy_num = int(input("anna jokin toinen kokonais luku (kirjoita 0 lopettaaksesi): "))
    
jarjesta()
    
