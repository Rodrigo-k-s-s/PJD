'''
Lucas Guimarães
Guilherme Manja
Rodrigo Kenji
'''

dois = 0
cinco = 0
dez = 0
vinte = 0
cinquenta = 0
cem = 0
duzentos = 0

nome = input('Boa tarde! Qual é o seu nome? ')
saldo = 2339
retirar = int(input(f'Olá {nome}, você tem R${saldo:.2f} de saldo. Quanto deseja retirar? '))

 
if saldo > retirar:

    while True:
        if retirar >=  200:
            retirar -= 200
            duzentos += 1
        elif retirar >= 100:
            retirar -= 100
            cem += 1
        elif retirar >= 50:
            retirar -= 50
            cinquenta += 1
        elif retirar >= 20:
            retirar -= 20
            vinte += 1
        elif retirar >= 10:
            retirar -= 10
            dez += 1
        elif retirar >= 5:
            retirar -= 5
            cinco += 1
        elif retirar >= 2:
            retirar -= 2
            dois += 1
        else:
            break

    print(f'Notas de R$200: {duzentos}')
    print(f'Notas de R$100: {cem}')
    print(f'Notas de R$50: {cinquenta}')
    print(f'Notas de R$20: {vinte}')
    print(f'Notas de R$10: {dez}')
    print(f'Notas de R$5: {cinco}')
    print(f'Notas de R$2: {dois}')
else:
    print('Saldo insuficiente')
