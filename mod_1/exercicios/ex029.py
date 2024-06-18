velocidade = int(input('Digite a velocidade do carro: '))

if velocidade < 80:
    print('Tenha um bom dia! Continue dirigindo com segurança!')
else:
    multa = (velocidade - 80) * 7
    print('MULTADO! Você excedeu o limite de velocidade permitido de 80km/h.')
    print('Você deve pagar multa de R${}.00!'.format(multa))