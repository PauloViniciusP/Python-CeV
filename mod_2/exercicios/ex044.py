print('{:-^60}'.format('Lojas Nascimento'))
preço = float(input('Preço das compras: R$'))
print('''Formas de pagamento:
[1] à vista dinheiro
[2] à vista cartão
[3] 2x cartão
[4] 3x ou mais no cartão''')

opção = int(input('Digite a opção: '))

if opção == 1:
    total = preço - (preço * 10/100)
elif opção == 2:
    total = preço - (preço * 5/100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}, sem juros.'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20/100)
    prestacoes = int(input('Quantas prestações? '))
    if prestacoes >= 3:
        parcela = total / prestacoes
        print('Sua compra será parcelada em {}x de R${:.2f}, com juros'.format(prestacoes, parcela))
    else:
        print('Número de prestações inválido. Tente novamente.')
else:
    total = preço
    print('Opção \033[31m inválida \033[m de pagamento. Tente novamente.')   

print('Sua compra de R${:.2f} vai custar R${:.2f} nessas condições.'.format(preço, total))