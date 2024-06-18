salario = float(input('Digite o valor do salário: '))

if salario <= 1250:
    aumento = salario * 0.15
else:
    aumento = salario * 0.1

print('Para o salário de R${:.2f}, o valor do aumento será de R${:.2f}, totalizando um novo salário de R${:.2f}'.format(salario, aumento, (salario+aumento)))