'''
Změň program Kámen, Nůžky, Papír tak, aby opakoval hru, dokud uživatel nezadá slovo konec.
'''

import random
seznam = ['kámen','nůžky','papír']

tah_pocitace = random.choice (seznam)
tah_cloveka = input('kámen, nůžky, papír?')
print ('tah_pocitace', tah_pocitace)
print ('tah_cloveka', tah_cloveka)

while True:
    if tah_pocitace == 'kámen':
        if tah_cloveka == 'kámen':
            print('Plichta.')
        elif tah_cloveka == 'papír':
            print('Vyhrál člověk.')
        elif tah_cloveka == 'nůžky':
            print('Vyhrál počítač.')

    if tah_pocitace == 'nůžky':
        if tah_cloveka == 'nůžky':
            print('Plichta.')
        elif tah_cloveka == 'kámen':
            print('Vyhrál člověk.')
        elif tah_cloveka == 'papír':
            print('Vyhrál počítač.')


    if tah_pocitace == 'papír':
        if tah_cloveka == 'papír':
            print('Plichta.')
        elif tah_cloveka == 'nůžky':
            print('Vyhrál člověk.')
        elif tah_cloveka == 'kámen':
            print('Vyhrál počítač.')

    if tah_cloveka == ('konec'):
        print ('konec')
        break

    tah_pocitace = random.choice (seznam)
    tah_cloveka = input('kámen, nůžky, papír?')
    print ('tah_pocitace', tah_pocitace)
    print ('tah_cloveka', tah_cloveka)
