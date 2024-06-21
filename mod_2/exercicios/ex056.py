media = 0
mais = 0
menos = 0
nome_velho = ''

for i in range(1, 5):
    print('{:-^30}'.format('{}ª Pessoa').format(i))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    media += idade
    
    if sexo in 'Mm' and i == 1:
        mais = idade
    elif sexo in 'Mm' and idade > mais:
        mais = idade
        nome_velho = nome
    elif sexo in 'Ff' and idade < 20:
        menos += 1
media = media / 5

print('A média de idade do grupo é {}'.format(media))
print('O idade do homem mais velho é {} anos e ele se chama {}.'.format(mais, nome_velho))
print('Existem ao todo {} mulheres com menos de 20 anos.'.format(menos))
