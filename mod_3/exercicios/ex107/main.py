import currency

p = float(input('Digite o preço: R$'))
print(f'A metade de R${p} é R${currency.metade(p)}')
print(f'O dobro de R${p} é R${currency.dobro(p)} ')
print(f'Aumentando 20%, temos R${currency.aumentar(p, 20)}')
