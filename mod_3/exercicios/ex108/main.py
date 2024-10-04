import currency as cs

p = float(input('Digite o preço: R$'))
print(f'A metade de {cs.moeda(p)} é {cs.moeda(cs.metade(p))}')
print(f'O dobro de {cs.moeda(p)} é {cs.moeda(cs.dobro(p))} ')
print(f'Aumentando 20%, temos {cs.moeda(cs.aumentar(p, 20))}')
