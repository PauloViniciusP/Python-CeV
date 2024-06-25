from time import sleep
num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
opção = 0
while opção != 5:
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Encerrar programa''')
    opção = int(input('Qual sua escolha? '))
    if opção == 1:
        soma = num1 + num2
        print('A soma entre {} e {} é igual a {}'.format(num1, num2, soma))
    elif opção == 2:
        produto = num1 * num2
        print('O produto entre {} e {} é igual a {}'.format(num1, num2, produto))
    elif opção == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print('O número {} é o maior entre os dois valores'.format(maior))
    elif opção == 4:
        print('Informe os números novamente: ')
        num1 = int(input('Primeiro número: '))
        num2 = int(input('Segundo número: '))
    elif opção == 5:
        print('Encerrando programa.')
        sleep(1)
    else:
        print('Escolha inválida. Tente novamente.')
    print('-=-' * 15)
print('Fim do programa.')
