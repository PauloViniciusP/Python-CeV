from random import choice
print('-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-')
print("Adivinhe o número entre 0 e 5 que vou pensar. Tente a sorte!")
print('-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-')
numero = [0, 1, 2, 3, 4 , 5]
numero = choice(numero)

palpite = int(input('Tente chutar o número entre 0 e 5 que eu pensei: '))

if (palpite == numero):
    print('Acertou o número! Ambos pensamos em {}.'.format(palpite))
else:
    print('Não foi dessa vez! Você chutou {} e eu pensei em {}.'.format(palpite, numero))