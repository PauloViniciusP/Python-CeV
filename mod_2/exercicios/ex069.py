maiorDeIdade = qtdHomens = mulheresMenos20 = total =  0

while True:
    print('-' * 25)
    print(f'{'Registro de pessoas':_^25}')
    print('-' * 25)

    total += 1
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]

    if idade > 18:
        maiorDeIdade += 1
    if sexo == 'M':
        qtdHomens += 1
    if sexo == 'F' and idade < 20:
        mulheresMenos20 += 1

    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Quer continuar registrando? [S/N] ')).strip().upper()[0]
    if escolha == 'N':
        break

print(f'\nTotal de pessoas registradass: {total}.')
print(f'Total de pessoas com mais de 18 anos: {maiorDeIdade}.')
print(f'Total de homens registradas: {qtdHomens}.')
print(f'Total de mulheres com menos de 20 anos: {mulheresMenos20}.')
