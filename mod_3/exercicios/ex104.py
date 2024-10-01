def leiaInt(msg):
    check = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            check = True
        else:
            print('\033[0;31mErro! Digite um número inteiro válido.\033[m')
        if check:
            break
    return valor


# main program
num = leiaInt('Digite um número: ')
print(f'Você digitou o número inteiro {num}')
