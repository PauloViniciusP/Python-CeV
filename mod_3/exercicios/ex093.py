jogador = dict()
quantgols = list()

jogador['nome'] = str(input('Nome do Jogador: '))
quantjogos = int(input(f'Quantas partidas {jogador['nome']} jogou? '))

for p in range(0, quantjogos):
    quantgols.append(int(input(f'Quantos gols na partida {p+1}? ')))
   
jogador['gols'] = quantgols[:]
jogador['total'] = sum(quantgols)
print('-=-' * 20)
print(jogador)
print('-=-' * 20)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor de {v}')\

print('-=-' * 20)

print(f'O jogador {jogador['nome']} jogou {len(jogador["gols"])} partidas.')

for i, g in enumerate(jogador['gols']):
    print(f'    => Na partida {i+1}, fez {g} gols. ')
print(f'Com um total de {jogador['total']} gols.')
