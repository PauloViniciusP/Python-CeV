peso = float(input('Qual seu peso: (KG)'))
altura = float(input('Qual sua altura: (m)'))

imc = peso / (altura ** 2)
print('O IMC dessa pessoa é {:.2f}'.format(imc))

if imc < 18.5:
    print('Você está na faixa abaixo do peso.')
elif imc <= 25:
    print('Você está na faixa de peso ideal.')
elif imc <= 30:
    print('Você está na faixa de sobrepeso.')
elif imc <= 40:
    print('Você está na faixa de obsidade.')
else:
    print('Você está na faixa de obsidade mórbida.')