print('Super Gerador de termos de PA')
primeiro = int(input('Primeiro termo da PA: '))
razão = int(input('Razão da PA: '))
cont = 1
termo = primeiro
mais = 10
total = 0

print('-=-' * 10)
print('Os Termos da PA: ')


while mais != 0:
    total = total + mais
    while cont <= total:
        print('{}'.format(termo), end='')
        print(' -> ' if cont < total else '', end='')
        termo += razão
        cont += 1
    mais = int(input('\nQuantos termos a mais quer mostrar? '))
print('O programa exibiu {} termos de uma PA'.format(total))
