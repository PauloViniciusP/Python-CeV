soma = 0
contador = 0
for i in range(1, 7):
    numero = int(input('Digite o {}º número: '.format(i)))
    if numero % 2 == 0:
        soma += numero
        contador += 1
print('A soma dos {} números pares digitados é: {}'.format(contador, soma))