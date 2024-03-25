"""
Naprogramuj hádání čísla: počítač vygeneruje náhodné číslo z rozsahu 1 až 100, ale nevypíše ho. Nechá uživatele v cyklu se ptát na to číslo a vypíše pouze informaci, jestli je hádané číslo větší nebo menší než náhodné číslo.
"""

from random import randrange

hadane_cislo = randrange(101)

while True:
    cislo_pokus = int(input("Hádej číslo: "))
    if cislo_pokus == hadane_cislo:
        print("Super!")
        break
    elif cislo_pokus < hadane_cislo:
        print("Zkus víc")
    else:
        print("Zkus míň")
