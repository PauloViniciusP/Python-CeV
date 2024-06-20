soma = 0
contador = 0
for numero in range(1, 501):
    if numero % 2 != 0:
        if numero % 3 == 0:
            contador += 1
            soma += numero 
print('A soma de todos os {} valores encontrados é {}'.format(contador, soma))