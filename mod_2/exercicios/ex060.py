numero = int(input('Digite um número para calcular o fatorial: '))
cont = numero
fatorial = 1

print('Calculando {}! = '.format(numero), end='')
while cont != 0:
    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
    fatorial *= cont
    cont -= 1
print('{}'.format(fatorial))
