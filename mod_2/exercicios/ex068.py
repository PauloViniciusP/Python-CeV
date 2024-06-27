from random import randint

cont = 0

print('-=-' * 10)
print('Vamos jogar PAR ou ÍMPAR!')
print('-=-' * 10)

while True:
    valor = int(input('Digite um valor: '))
    computador = randint(0, 9)
    soma = valor + computador
    escolha = ' '
    
    while escolha not in 'PI':
        escolha = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]

    print('-' * 30)
    print(f'Você jogou {valor} e computador jogou {computador}. O total foi {soma}.', end=' ')
    print('Deu par!' if soma % 2 == 0 else 'Deu impar!')
    
    if soma % 2 == 0:
        if escolha in 'P':
            print('Você Venceu!')
            cont += 1
        else:
            print('Você perdeu!')
            break
    else:
        if escolha in 'I':
            print('Você Venceu!')
            cont += 1
        else:
            print('Você perdeu!')
            break
    print('-=-' * 10)
    print('Vamos jogar novamente!')

if cont == 1:
    print(f'Game Over! Você venceu {cont} vez consecutiva.')
else:
    print(f'Game Over! Você venceu {cont} vezes consecutivas.')
