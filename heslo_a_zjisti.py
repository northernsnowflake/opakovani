'''
Napiš program, který se zeptá uživatele na heslo a zjistí, jestli:

heslo obsahuje minimálně 1 malé písmeno
heslo obsahuje minimálně 1 velké písmeno
heslo obsahuje minimálně jeden speciální znak: +@#$%^&*
heslo neobsahuje ani jednu mezeru
Pokud heslo nesplňuje aspoň jednu z těchto podmínek, program poinformuje o tom uživatele, a ukončí se. Pokud je heslo správně (= splňuje všechny podmínky), program řekne uživateli tajemství.
'''


'''
heslo = input('Zadej heslo: ')
specialni_znak = '+@#$%^&*'
mezera = ' '

count_low = 0
count_up = 0
count_specialni = 0

for znak in heslo:
    if znak.islower():
        count_low = count_low+1

for znak in heslo:
    if znak.isupper():
        count_up = count_up+1

for znak in heslo:
    if znak in specialni_znak:
        count_specialni = count_specialni + 1

if ' ' in heslo:
    print('Mezera')

if count_low < 1 or count_up < 1 or count_specialni < 1 or ' ' in heslo :
    print('Nesplněny podmínky')

if count_low >= 1 and count_up >= 1 and count_specialni >= 1 and ' ' not in heslo:
    print('Tajemstvi je tu')
'''

"-- uprava --"

heslo = input('Zadej heslo: ')
specialni_znak = '+@#$%^&*'
mezera = ' '

count_low = 0
count_up = 0
count_specialni = 0

for znak in heslo:
    if znak.islower():
        count_low = count_low+1
    if znak.isupper():
        count_up = count_up+1   
    if znak in specialni_znak:
        count_specialni = count_specialni+1
    if ' ' in heslo:
        print('Mezera')
if count_low < 1 or count_up < 1 or count_specialni < 1 or ' ' in heslo :
    print('Nesplněny podmínky')
if count_low >= 1 and count_up >= 1 and count_specialni >= 1 and ' ' not in heslo:
    print('Tajemstvi je tu')

