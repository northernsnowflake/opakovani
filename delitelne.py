"""
Napiš program, který vypíše čísla od jedné do 100, ale:

Pokud je číslo dělitelné třemi, napíše místo něj „bum”.
Pokud je číslo dělitelné pěti, napíše místo něj „bác”.
Pokud je číslo dělitelné pěti i třemi zároveň, napíše místo toho „bum-bác”.
"""

from random import randrange

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print('bum-bác', end="\n")
    elif i % 3 == 0:
    #    print('bum')
        print('bum', end="\n")
    elif i % 5 == 0:
        print('bác', end="\n")
    else:
        print(i, end="\n")
