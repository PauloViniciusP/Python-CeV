from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    
    print('-=-' * 15)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(1)
    
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            cont += p
            sleep(0.5)
        print('Fim!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            cont -= p
            sleep(0.5)
        print('Fim!')
  

# main program
contador(1, 10, 1)
contador(10, 0, 2)
print('Escolha sua contagem personalizada: ')
ini = int(input('Início: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)
print('-~-' * 15)  
