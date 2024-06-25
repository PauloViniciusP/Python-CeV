numero = soma = cont = 0

while numero != 999:
    numero = int(input('Digite um número: [999 para parar] '))
    if numero != 999:
        soma += numero
        cont += 1
print('A soma dos {} números digitados é {}'.format(cont, soma))
