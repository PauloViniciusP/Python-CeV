casa = float(input('Informe o valor da casa: '))
salario = float(input('Informe o salário do comprador: '))
prazo = int(input('Informe o prazo, em anos, para o financiamento: '))

parcela = casa / (prazo * 12)
print('Para pagar uma casa de RS{:.2f} em {} anos'.format(casa, prazo), end='')
print('a parcela será de R${:.2f}'.format(parcela))

if (salario * 0.3) >=  parcela:
    print('Empréstimo aprovado!')
else:
    print('Empréstimo negado.')