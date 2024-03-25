#Napiš program, který se zeptá na 3 čísla a zjistí,
#jestli je jejich součet větší než 10.

'''
prvni = int(input('První číslo:'))
druhe = int(input('Druhé číslo:'))
treti = int(input('Třetí číslo:'))

soucet = prvni + druhe + treti
if soucet > 10:
    print('Soucet je vetsi nez 10')
else:
    print('Soucet je mensi nebo rovno 10')
'''

# Úprava: program se má zeptat na 10 čísel a zjistit, jestli je součet větší než tisíc
seznam = range(0,10)
cisla = []
soucet = 0

for prvek in seznam:
    cislo = int(input('cislo je:'))
    cisla.append(cislo)
    #print(cisla)
#print(cisla)
for kazde in cisla:
    soucet = soucet + kazde
if soucet > 1000:
    print('Soucet je vetsi nez 1000')
else:
    print('Soucet je mensi nebo rovno 1000')
