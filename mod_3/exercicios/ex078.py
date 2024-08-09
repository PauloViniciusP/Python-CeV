values = []

for i in range(0, 5):
    values.append(int(input(f'Digite um valor para a posição {i+1}: ')))

    if i == 0:
        maior = menor = values[0]
    else:
        if maior < values[i]:
            maior = values[i]
        if menor > values[i]:
            menor = values[i]

print(f'Você digitou os valores: {values}')
print(f'O maior valor digitado foi {maior}, na posição: ', end='')
for c, v in enumerate(values):
    if v == maior:
        print(f'{c+1}°... ', end='')
print(f'\nO menor valor digitado foi {menor}, na posição: ', end='')
for c, v in enumerate(values):
    if v == menor:
        print(f'{c+1}°..  ', end='')
