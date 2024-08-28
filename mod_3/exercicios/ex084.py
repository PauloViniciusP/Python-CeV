temp = []
dados = []
maior = menor = 0

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(dados) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]        

    dados.append(temp[:])
    temp.clear()

    escolha = str(input('Deseja continuar? '))
    if escolha in 'Nn':
        break

print(f'Foram cadastradas {len(dados)} pessoas.')
print(f'O maior peso foi {maior}kg. Peso de: ', end='')
for d in dados:
    if d[1] == maior:
        print(f'[{d[0]}]', end='')

print(f'\nO menor peso foi de {menor}kg. Peso de: ', end='')
for d in dados:
    if d[1] == menor:
        print(f'[{d[0]}]')
