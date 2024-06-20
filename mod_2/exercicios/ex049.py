tabuada = int(input('Digite um número para ver sua tabuada: '))
print('-=-' * 5)
for i in range(0, 11):
    multiplicação = tabuada * i
    print('{} x {:2} = {:2}'.format(tabuada, i, multiplicação))
print('-=-' * 5)