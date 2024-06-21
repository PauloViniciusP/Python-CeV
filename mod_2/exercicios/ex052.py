numero = int(input('Digite um número: '))
total_divisões = 0
for i in range (1, numero + 1):
    if numero % i == 0:
        print(' \033[36m', end='')
        total_divisões += 1
    else:
        print(' \033[31m', end='')
    print('{}'.format(i), end='')

print('\n\033[mO número {} foi divisível {} vezes'.format(numero, total_divisões))
if total_divisões == 2:
    print('E por isso esse número é primo.')
else:
    print('E por isso esse número não é primo.')
