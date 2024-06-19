from datetime import date

nascimento = int(input('Ano de nascimento: '))
anoatual = date.today().year
idade = anoatual - nascimento
print('Quem nasceu em {} tem {} anos em {}.'.format(nascimento, idade, anoatual))

if idade < 18:
    diferenca = 18 - idade
    print('Ainda faltam {} anos para o alistamento.'.format(diferenca))
    print('Seu alistamento será em {}.'.format(anoatual + diferenca))
elif idade > 18:
    diferenca = idade - 18
    print('Você deveria ter se alistado há {} anos.'.format(diferenca))
    print('Seu alistamento foi em {}.'.format(anoatual - diferenca))
else:
    print('Você tem que se alistar imediatamente!')