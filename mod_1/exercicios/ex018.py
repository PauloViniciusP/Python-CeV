import math
num = float(input('Digite um número: '))
seno = math.sin(math.radians(num))
cos = math.cos(math.radians(num))
tan = math.tan(math.radians(num))
print('O angulo de {}° tem o seno de {:.2f}'.format(num, seno))
print('O angulo de {}° tem o cosseno de {:.2f}'.format(num, cos))
print('O angulo de {}° tem a tangente de {:.2f}'.format(num, tan))
