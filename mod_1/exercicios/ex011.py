largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura
print('Sua parede tem dimensão {}mx{}m e área de {}m²'.format(largura, altura, area))
print('Para pintar essa parede vai precisar de {:.3f}l de tinta'.format(area/2))
