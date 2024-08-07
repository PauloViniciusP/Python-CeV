valor = (int(input('Digite o primeiro valor: ')),
          int(input('Digite o segundo valor: ')),
          int(input('Digite o terceiro valor: ')),
          int(input('Digite o quarto valor: ')))

print(f'Você digitou os valores: {valor}')
print(f'O valor 9 apareceu {valor.count(9)} vezes')

if 3 in valor:
    print(f'O primeiro valor 3 foi digitado na posição: {valor.index(3)+1}')
else:
    print('O valor 3 não apareceu em qualquer posição')

print(f'Os valores pares digitados foram: ')
for n in valor:
    if n % 2 == 0:
        print(n, end=' ')
