print('Gerador de termos de PA')
primeiro = int(input('Primeiro termo da PA: '))
razão = int(input('Razão da PA: '))
cont = 1
termo = primeiro
print('-=-' * 10)
print('Os Termos da PA: ')

while cont <= 10:
    print('{}'.format(termo), end='')
    print(' -> ' if cont < 10 else '', end='')
    termo += razão
    cont += 1
