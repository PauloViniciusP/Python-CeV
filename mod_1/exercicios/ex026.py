nome = str(input('Qual seu nome completo?')).strip()
nome = nome.split()
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))