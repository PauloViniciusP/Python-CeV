comp = [[], []]
valor = 0

for i in range(1, 8):
    valor = int(input(f'Digite o {i}o valor: '))
    if valor % 2 == 0:
        comp[0].append(valor)
    else:
        comp[1].append(valor)

print('-=-' * 15)
comp[0].sort()
comp[1].sort()

print(f'Os valores pares digitados foram: {comp[0]}')
print(f'Os valores ímpares digitados foram: {comp[1]}')
