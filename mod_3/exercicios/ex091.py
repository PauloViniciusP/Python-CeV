from random import randint
from time import sleep
from operator import itemgetter

jogo = dict()
ranking = list()

for i in range(1, 5):
    jogo[f'Jogador{i}'] = randint(1, 6)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

for j, v in jogo.items():
    print(f'O {j} tirou {v} no lançamento do dado')
    sleep(1)

print('-=-' * 20)
print(f'{'  Ranking dos Jogadores  ':=^29}')

for i, v in enumerate(ranking):
    print(f'  {i+1}° lugar: {v[0]} com {v[1]}')
    sleep(1)
