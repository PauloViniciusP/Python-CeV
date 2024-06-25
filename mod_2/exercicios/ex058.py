from random import randint

print('''Sou seu computador e acabei de pensar em um número entre 0 e 10.
Será que consegue adivinhar qual foi?
''')
cont = 0
acertou = False
computador = randint(0, 10)

while not acertou:
    palpite = int(input('Qual seu palpite? '))
    cont += 1
    if palpite == computador:
        acertou = True
    else:
        if palpite > computador:
            print('Menos! Tente mais uma vez.')
        elif palpite < computador:
            print('Mais! Tente mais uma vez.')
        
print('Parabéns! Você acertou depois de {} tentativas.'.format(cont))
