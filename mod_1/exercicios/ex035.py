lado1 = float(input('Digite o tamanho do primeiro lado do triangulo: '))
lado2 = float(input('Digite o tamanho do segundo lado do triangulo: '))
lado3 = float(input('Digite o tamanho do terceiro lado do triangulo: '))

if lado1 >= lado2 + lado3 or lado2 >= lado1 + lado3 or lado3 >= lado1 + lado2:
    print('É impossível formar um triângulo com os segmentos de reta informados.')
else:
    print('É possível formar um triângulo com os segmentos de reta informados.')