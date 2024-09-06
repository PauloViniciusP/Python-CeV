time = list()
jogador = dict()
partida = list()

while True:
    jogador.clear()
    partida.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    quantpartidas = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
    for p in range(0, quantpartidas):
        partida.append(int(input(f'Quantos gols na partida {p+1}? ')))
    jogador['gols'] = partida[:]
    jogador['total_gols'] = sum(partida)
    time.append(jogador.copy())
    
    while True:
        resp = str(input('Deseja continuar? [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas com S ou N.')
    if resp == 'N':
        break
print('---' * 20)

print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('---' * 20)

for i, v in enumerate(time):
    print(f'{i:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-=-' * 20)

while True:
    busca = int(input('Mostrar dados de qual jogador? (999: finaliza a busca): '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f'--- Levantamento do jogador {time[busca]['nome']}: ')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
        print(f' -- Com um total de {time[busca]['total_gols']} gols na temporada.')
    print('===' * 20)
print('<< Busca Finalizada >>')
