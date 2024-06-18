distancia = float(input('Digite a distância da viagem em KM: '))

print('Sua viagem de {}KM começará em breve.'.format(distancia))
if distancia < 200:
    preco = distancia * 0.5
else:
    preco = distancia * 0.45    
print('O preço da passagem será R${:.2f}'.format(preco))