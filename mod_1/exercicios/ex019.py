from random import choice
n1 = str(input('Primeiro aluno:'))
n2 = str(input('Segundo aluno:'))
n3 = str(input('Terceiro aluno:'))
n4 = str(input('Quarto aluno:'))

lista_nomes = [n1, n2, n3, n4]

sorteado = choice(lista_nomes)

print('O nome do aluno sorteado é {}'.format(sorteado))
