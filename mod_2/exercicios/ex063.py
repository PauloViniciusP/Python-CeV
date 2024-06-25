print('=-=' * 8)
print(' Sequência de Fibonacci')
print('=-=' * 8)

numero = int(input('Quantos termos da sequência de Fibonacci deseja exibir? '))
t1 = 0
t2 = 1
cont = 3

print('~-~' *  10)
print('{} -> {}'.format(t1, t2), end='')

while cont <= numero:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    print('-> {} '.format(t3), end='')
    cont += 1
