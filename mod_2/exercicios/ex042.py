lado1 = float(input('Digite o tamanho do primeiro segmento de reta: '))
lado2 = float(input('Digite o tamanho do segundo segmento de reta: '))
lado3 = float(input('Digite o tamanho do terceiro segmento de reta: '))

if lado1 >= lado2 + lado3 or lado2 >= lado1 + lado3 or lado3 >= lado1 + lado2:
    print('É impossível formar um triângulo com os segmentos de reta informados.')
elif lado1 == lado2 == lado3:
    print('Os segmentos de reta acima podem formar um triângulo equilátero.')
elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
    print('Os segmentos de reta acima podem formar um triângulo escaleno')
else:
    print('Os segmentos de reta acima podem formar um triângulo isósceles.')
    