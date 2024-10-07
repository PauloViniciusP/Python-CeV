import currency as cs

p = float(input('Digite o preço: R$'))
print(f'A metade de {cs.moeda(p)} é {cs.metade(p, True)}')
print(f'O dobro de {cs.moeda(p)} é {cs.dobro(p, True)} ')
print(f'Aumentando 20%, temos {cs.aumentar(p, 20, True)}')
print(f'Reduzindo 15%, temos {cs.diminuir(p, 15, True)}')
