total = pcaro = pbarato = qtd = 0
nomepbarato = ' '

print('-=-' * 10)
print(f'{'Lojas Trem Bão':^30}')
print('-=-' * 10)

while True:
    nomep = str(input('Nome do produto: ')).strip()
    preço = float(input('Preço: R$'))
    qtd += 1
    total += preço
    
    if preço > 1000:
        pcaro += 1
    
    if qtd == 1 or preço < pbarato:
        pbarato = preço
        nomepbarato = nomep
    
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

print('\n{:-^40}'.format('Calculando resultados:'))
print(f'O gasto total da compra foi de R${total:.2f}, com total de {qtd} produtos')
print(f'Na qual {pcaro} produtos custaram acima de R$1000')
print(f'{nomepbarato} foi o produto mais barato, custando {pbarato:.2f}')
