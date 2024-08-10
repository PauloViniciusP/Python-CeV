values = list()

while True:
    value = int(input('Digite um valor: '))
    if value not in values:
        values.append(value)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor repetido. Não foi adicionado!')

    choice = str(input('Deseja continuar? [S/N]: ')).lower()
    if choice in 'n':
        break

values.sort()

print('-=-'*15)
print(f'Os valores digitados foram: {values}')
