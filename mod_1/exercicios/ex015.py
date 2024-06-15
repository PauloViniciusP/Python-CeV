qtdDias = int(input('Qual a quantidade de dias alugado?'))
qtdKM = int(input('Qual a quantidade de KM percorridos?'))
preco = (qtdKM * 0.15) + (qtdDias * 60)
print('O preço por {} dias e {}KM, fica em R${:.2f}'.format(qtdDias, qtdKM, preco))
