salario = float(input('Qual o salário do funcionário? R$'))
aumento = salario + (salario* 15/100)
print('Um funcionário que ganhava {:.2f}, com 15% de aumento, passa a ganhar R${:.2f}'.format(salario, aumento))
