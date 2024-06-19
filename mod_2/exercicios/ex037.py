numero = int(input('Digite um número para conversão: '))
print('''Escolha a base para conversão: ')
[1] Binário
[2] Octal
[3] Hexadecimal''')

base = int(input('Sua base para conversão: '))
if base == 1:
    print('{} convertido para Binário é igual a {}'.format(numero, bin(numero)[2:]))
elif base == 2:
    print('{} convertido para Octal é igual a {}'.format(numero, oct(numero)[2:]))
elif base == 3:
    print('{} convertido para Hexadecimal é igual a {}'.format(numero, hex(numero)[2:]))
else:
    print('Opção inválida! Tente novamente.')