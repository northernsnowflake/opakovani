"""
Napiš program, který vyzve uživatele k zadání řetězce složeného z otevíracích a zavíracích závorek jednoho typu, např. (). Program ověří, jestli jsou závorky správně, to znamená každá otevřená závorka je uzavřena, a výsledek vypíše. Pokud program narazí na jiný znak než závorky, vypíše chybu a ukončí se.

Příklad:

()(()(())) je správně
())( je špatně
Bonus: vypiš index znaku, kde program odhalil chybu v řetězci
"""


hadane_pozice = []
hadane_pozice2 = []
retezec = input('Zadej řetězec složeného z otevíracích nebo zavíracích závorek jednoho typu: ')

leva = '('
prava = ')'

pozice_leve = retezec.find(leva)
while pozice_leve != -1: # dokud tam nějaká je
    hadane_pozice.append(pozice_leve)
    print(pozice_leve)
    pozice_leve = retezec.find(leva, pozice_leve + 1)
    #if hadane_pozice
    #print(pozice_leve)
print(hadane_pozice)
#print(f'Pozice leve {pozice_leve}')

pozice_prave = retezec.find(prava)
while pozice_prave != -1:
    hadane_pozice2.append(pozice_prave)
    print(pozice_prave)
    pozice_prave = retezec.find(prava, pozice_prave + 1)
print(hadane_pozice2)
#print(f'Pozice prave {pozice_prave}')


if len(hadane_pozice) == len(hadane_pozice2):
    balanced = True
    for i in range(len(hadane_pozice)):
        if hadane_pozice[i] > hadane_pozice2[i]:
            balanced = False
            break
    if balanced:
        print(f'{retezec} je správně (vyvážené závorky)')
    else:
        print(f'{retezec} je špatně (nezávorkované nebo nevyvážené závorky)')
else:
    print(f'{retezec} je špatně (nezávorkované nebo nevyvážené závorky)')