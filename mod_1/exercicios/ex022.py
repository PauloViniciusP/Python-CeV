nome = str(input('Digite seu nome completo:')).strip()
print('Seu nome em letras maiúsculas é {}'.format(nome.upper()))
print('Seu nome em letras minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))

nome_separado = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(nome_separado[0], len(nome_separado[0])))