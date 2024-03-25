"""
Bonus:

místo ukládání jednoho řetězce do proměnné, použij seznam několika řetězcu, v Pythonu se vytváří takto: muj_seznam = ["test", "admin", "maruska"]
se seznamem můžeš pracovat velmi podobně jako s řetězci, tzn.

můžeš přístupovat k jednotlivým prvkům pomocí indexů - vyzkoušej si např. muj_seznam[0]
můžeš procházet seznam pomocí for cyklu
můžeš zjistit, jestli je daný prvek obsažen v seznamu pomocí operátoru in, např.
>>> "maruska" in muj_seznam
True
>>> "maru" in muj_seznam
False
"""

jmeno = input('Zadej jméno: ')
databaze = ["test", "admin", "maruska"]

#print(databaze[0])
while jmeno not in databaze:
    jmeno = input('Zadej jméno: ')
    if jmeno in databaze:
        print('Trefa')
        break

if "maru" in databaze:
    print(True)
else:
    print(False)