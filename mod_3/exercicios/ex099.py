from time import sleep


def maior(* num):
    cont = maior = 0
    print('-=-' * 15)
    print(f'{'Analisando os valores informados:':^45} ')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0 or valor > maior:
            maior = valor
        cont += 1 
    
    print(f'\nForam informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')
    


# main program 
maior(2, 9, 14, 5, 7, 1)
maior(4, 7, 11, 0)
# maior(1, 2)
# maior(6)
# maior()