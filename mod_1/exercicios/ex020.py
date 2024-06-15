from random import shuffle

nome_1 = str(input('Nome do primeiro aluno:'))
nome_2 = str(input('Nome do segundo aluno:'))
nome_3 = str(input('Nome do terceiro aluno:'))
nome_4 = str(input('Nome do quarto aluno:'))

nomes = [nome_1, nome_2, nome_3, nome_4]

shuffle(nomes)

print('A ordem de sorteio será: {}'.format(nomes))