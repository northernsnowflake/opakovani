'''
vyber nahodna cislo 1 az 6, dokud nepadne 6
vypis kolik má bodů
ukládej kdo vede a kolik má bodů
další hráč

'''
from random import randrange

vyhrava = 0
vitez = 0

for i in range(1,5):
    kolikrat_hazel = 0
    aktualni_hod = 0
    while aktualni_hod != 6:
        aktualni_hod = randrange(1,7)
        kolikrat_hazel+=1
        #print(f'Hází hráč {i} a hodil {aktualni_hod}')
    if kolikrat_hazel > vyhrava:
        vyhrava = kolikrat_hazel
        vitez = i
    elif kolikrat_hazel == vyhrava:
        if i < vitez:
            vitez = i

    print(f'Hraje hráč {i} a házel {kolikrat_hazel}')

#print(f'První hráč házel {kolikrat_hazel}x')
print(f'Vyhrává hráč č. {vitez}, který házel {vyhrava}x')
