lado1 = float(input('Digite o tamanho do primeiro segmento de reta: '))
lado2 = float(input('Digite o tamanho do segundo segmento de reta: '))
lado3 = float(input('Digite o tamanho do terceiro segmento de reta: '))

if lado1 < lado2 + lado3 or lado2 < lado1 + lado3 or lado3 < lado1 + lado2:
    print('É possível formar um triângulo ', end = '')
    if lado1 == lado2 == lado3:
        print('equilátero com os segmentos de reta informados.')
    elif lado1 != lado2 != lado3 != lado1:
        print('escaleno com os segmentos de reta informados.')
    else:
        print('isósceles com os segmentos de reta informados.')
else:
    print('É impossível formar um triângulo com os segmentos de reta informados.')
    