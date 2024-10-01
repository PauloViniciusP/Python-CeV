def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg} x {comp} é de {a}m².')


# main program
print(f'{'Controle de área':^20}')
print('-' * 20)
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
area(largura, comprimento)
