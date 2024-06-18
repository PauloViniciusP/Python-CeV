from random import randint
print('-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-')
print("Adivinhe o número entre 0 e 5 que vou pensar. Tente a sorte!")
print('-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-')
numero = randint(0, 5)

palpite = int(input('Tente chutar o número entre 0 e 5 que eu pensei: '))

if (palpite == numero):
    print('Acertou o número! Ambos pensamos em {}.'.format(palpite))
else:
    print('Não foi dessa vez! Você chutou {} e eu pensei em {}.'.format(palpite, numero))