from datetime import date
ano_atual = date.today().year
maior = 0
menor = 0
for i in range(1, 8):
    nascimento = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(i)))
    idade = ano_atual - nascimento
    if idade > 18:
        maior += 1
    else:
        menor += 1

print('Existem {} maiores de idade e {} menores de idade'.format(maior, menor))
