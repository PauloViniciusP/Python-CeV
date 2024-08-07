materialEscolar = ('Lápis', 1.80,
                   'Borracha', 3,
                   'Canetas', 18.90,
                   'Caderno', 20.90,
                   'Estojo', 22,
                   'Compasso', 13.99,
                   'Mochila', 143.69,
                   'Transferidor', 6.70,
                   'Livro', 40.90,
                   'Tablet', 1200)

print('-'*40)
print(f'{"Material Escolar - Preços":^40}')
print('-'*40)

for i in range(0, len(materialEscolar)):
    if i % 2 == 0:
        print(f'{materialEscolar[i]:.<30}', end='')
    else:
        print(f'R${materialEscolar[i]:>8.2f}')

print('-'*40)
