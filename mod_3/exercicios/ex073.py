times = ('Flamengo', 'Palmeiras', 'São Paulo', 'Chapecoense', 'Atlético-PR', 'Atlético-MG',
        'Corinthians', 'Fluminense', 'Grêmio', 'Fortaleza', 'Internacional',
        'Bahia', 'Botafogo', 'Red Bull Bragantino', 'Atlético-GO', 'Cuiabá',
        'Vasco', 'Juventude', 'Criciúma', 'Vitória')

print('-=-' * 10)
print(f'Lista de times do Brasileirão: {times}')
print('-=-' * 10)
print(f'Os 5 primeiros da tabela: {times[0:5]}')
print('-=-' * 10)
print(f'Os últimos 4 times da tabela são: {times[-4:]}')
print('-=-' * 10)
print(f'Os times em ordem alfabética: {sorted(times)}')
print('-=-' * 10)
print(f'O Chapecoense está na {times.index('Chapecoense')+1}ª posição.')
