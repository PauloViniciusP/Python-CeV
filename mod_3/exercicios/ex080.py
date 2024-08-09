values = []
for i in range(0, 5):
    value = int(input('Digite um valor: '))
    if i == 0 or value > values[-1]:
        values.append(value)
        print('Valor adicionado ao final da lista de valores.')
    else:
        cont = 0
        while cont < len(values):
            if value <= values[cont]:
                values.insert(cont, value)
                print(f'Valor adicionado na posição {cont}')
                break
            cont += 1
            
print('-=-'*15)
print(f'Os valores digitados em ordem crescente foram {values}')
