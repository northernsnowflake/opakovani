"""
Rozšíření programu na uživatelské jméno a heslo. Použij stejnou "databázi" uživatelů jako předchozí úloze. Napiš program, který se zeptá uživatele na uživatelské jméno a heslo, a následně:

pokud uživatelské jméno neexistuje, zahlásí tento fakt a zeptá se uživatele, jestli chce jméno zase zadat
pokud uživatel řekne "ano", program ho vyzve k zadání jména a provede kontrolu, zda jméno existuje
v opačném případě, pokud uživatel řekne "ne", program se ukončí
pokud uživatelské jméno existuje, ale heslo neodpovídá pravidlům nastaveným v úloze č. 6, program se opět uživatele, jestli chce heslo zase zadat
pokud "ano", vyzve uživatele k zadání hesla a provede kontrolu.
v opačném případě, pokud uživatel řekne "ne", program se ukončí
na konci se vždy vypíše poděkování za použití programu (i v případě, že uživatel přerušil zadávání jména nebo hesla)
bonus: zařiď, aby počítač rozuměl odpovědím jako "ano", "ANO", "aNO", "a", "A" - a obdobně pro "ne", "NE", "Ne", "n", atp.
"""

jmeno = input('Zadej jméno: ')
databaze = ["test", "admin", "maruska"]
heslo = "Jedn@"

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
        count_specialni = count_specialni = 1

if ' ' in heslo:
    print('Mezera')

if count_low < 1 or count_up < 1 or count_specialni < 1 or ' ' in heslo :
    print('Nesplněny podmínky')



#print(databaze[0])
while jmeno not in databaze:
    znovu_jmeno = input('Zvolené jméno neexistuje. Chcete zadat jmeno znovu? ano/ne ')
    if znovu_jmeno == 'ano':
        jmeno = input('Zadej jméno: ')
        if jmeno in databaze:
            if count_low >= 1 and count_up >= 1 and count_specialni >= 1 and ' ' not in heslo:
                znovu_heslo = input('Zvolené heslo neodpovídá pravidlům. Chcete zadat heslo znovu? ano/ne ')
                if znovu_heslo == 'ano':
                    heslo = input('Zadej heslo: ')
                else:
                    break
    else:
        break


print('Děkuji za použití programu')
