lista = list()
listaPar = list()
listaImpar = list()

while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    if valor % 2 == 0:
        listaPar.append(valor)
    else:
        listaImpar.append(valor)
    
    escolha = str(input('Deseja continuar? [S/N]: '))
    if escolha in 'Nn':
        break
listaPar.sort()
listaImpar.sort()

print(f'A lista completa de valores: {lista}')
print(f'A lista de valores pares em ordem: {listaPar}')
print(f'A lista de valores ímpares em ordem: {listaImpar}')
