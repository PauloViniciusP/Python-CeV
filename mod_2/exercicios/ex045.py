from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('''Suas opções são:
[0] Pedra
[1] Papel
[2] Tesoura''')

jogador = int(input('Qual sua escolha? '))

if jogador in [0, 1, 2]:
    
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')

    print('-=-' * 10)
    print('O computador escolheu {}'.format(itens[computador]))
    print('O jogador escolheu {}'.format(itens[jogador]))
    print('-=-' * 10)

    if computador == 0: # Computador escolheu Pedra
        if jogador == 0:
            print('Empate!')
        elif jogador == 1:
            print('Jogador vence!')
        elif jogador == 2: 
            print('Computador vence!')
    elif computador == 1: # Computador escolheu Papel
        if jogador == 0:
            print('Computador vence!')
        elif jogador == 1:
            print('Empate!')
        elif jogador == 2:
            print('Jogador vence!')
    elif computador == 2: # Computador escolheu Tesoura
        if jogador == 0:
            print('Jogador vence!')
        elif jogador == 1:
            print('Computador vence!')
        elif jogador == 2:
            print('Empate!')
else:
    print('Jogada inválida. Tente novamente.')