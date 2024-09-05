galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))

    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')

    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())

    while True:
        resp = str(input('Deseja continuar? S/N ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=-' * 20)

print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'B) A média de idade é de {media:5.2f} anos.')
print('C) As mulheres cadastradas foram ', end='')
for g in galera:
    if g['sexo'] == 'F':
        print(f'{g['nome']} ', end='')
print()
print('D) Lista de pessoas com idade acima da média: ')
for g in galera:
    if g['idade'] >= media:
        print('    ', end='')
        for k, v in g.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')
