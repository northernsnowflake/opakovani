"""
Napiš program, který se zepta uživatele na uživatelské jméno,
a porovná ho se jménem, které je uloženo v jeho databázi. 
(Pro jednoduchost tvoje databáze bude zatím obsahovat jen 
jednoho uživatele - ulož si libovolné uživatelské jméno do
proměnné jako řetězec). Pokud uživatel nezadá jméno správně, 
program se zeptá znovu. Uživatel má 3 pokusy, pak se program ukončí."""

databaze = 'Nathaniel'

for i in range(3):
    jmeno = input('Zadej jméno: ')
    if jmeno == databaze:
        print('Trefa')
        break

# úprava 
# Uprav předchozí program: Program se bude uživatele ptát tak dlouho
# dokud nezadá správné (čili existující) uživatelské jméno.

jmeno = input('Zadej jméno: ')
databaze = 'Nathaniel'

if jmeno == databaze:
        print('Trefa')
while jmeno != databaze:
    jmeno = input('Zadej jméno: ')
    if jmeno == databaze:
        print('Trefa')
        break

