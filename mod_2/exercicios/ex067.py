while True:
    numero = int(int(input("Deseja exibir a tabuada de qual número? ")))
    print('-=-' *10)
    if numero < 0:
        print('Programa encerrado!')
        break
    for i in range (1, 11):
        print(f'{numero} x {i:2} = {numero * i:2}')
    print('-=-' * 10)