lista = []

while True:
    lista.append(int(input('Digite um valor: ')))
    escolha = str(input('Deseja continuar: [S/N] '))

    if escolha in 'Nn':
        break

lista.sort(reverse=True)

print(f'Foram digitados {len(lista)} elementos')
print(f'Os elementos em ordem decrescente são: {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não faz parte da lista')