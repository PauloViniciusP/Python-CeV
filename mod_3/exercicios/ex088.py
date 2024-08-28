from random import randint
from time import sleep

jogos = list()
sorteio = list()
total = 1

print('-=-' * 15)
print(f'{'Jogos da Mega Sena':^45}')
print('-=-' * 15)

quant = int(input('Quantos jogos você quer sortear? '))
while total <= quant:
    cont = 0
    while True:
        valor = randint(1, 60)
        if valor not in jogos:
            jogos.append(valor)
            cont += 1
        if cont >= 6:
            break
    
    jogos.sort()
    sorteio.append(jogos[:])
    jogos.clear()
    total += 1

print('-=-' * 2, f'Sorteando {quant} jogos', '-=-' * 2)
for i, j in enumerate(sorteio):
    sleep(1)
    print(f'Jogo {i+1}: {j}')   
print('-=-' * 3, 'Boa sorte!', '-=-' * 3)
