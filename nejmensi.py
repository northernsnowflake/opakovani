"""
Napiš program, který se ptá uživatele na čísla do té doby,
než zadá 0. Poté vypíše nejmenší ze zadaných čísel.
(Pozor: nula se mezi porovnávaná čísla nepočítá.)

Nápověda: průběžně stačí ukládat jen údaj, které číslo je aktuálně 
to nejmenší.
"""
aktualni_cislo = int(input('Zadej číslo: '))
nejmensi_cislo = 1000
while aktualni_cislo != 0:
    if aktualni_cislo < nejmensi_cislo:
        nejmensi_cislo = aktualni_cislo
    else:
        aktualni_cislo = int(input('Zadej číslo: '))

if aktualni_cislo == 0:
    pass

print(f'Nejmensi cislo je {nejmensi_cislo}')
