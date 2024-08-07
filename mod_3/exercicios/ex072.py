nomeNum = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 
           'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
           'cartoze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
           'dezenove', 'vinte')

while True:
    while True:
        numero = int(input('Digite um número entere 0 e 20: '))
        if 0 <= numero <= 20:
            break
        print('Tente novamente. ', end='')

    print(f'Você digitou o número {nomeNum[numero]}.')
    print('-' * 30)
    
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    
    if escolha == 'N':
        break
print('Programa finalizado com sucesso!')
