dados = list()

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    dados.append([nome, [nota1, nota2], media])

    resposta = str(input('Deseja continuar? [S/N]'))
    if resposta in 'Nn':
        break
print('-=-' * 20)
print(f'{'No.':<4}{'Nome':<10}{'Média':>8}')
print('-' * 60)
for i, d in enumerate(dados):
    print(f'{i:<4}{d[0]:<10}{d[2]:>8.1f}')

while True:
    print('-=-' * 20)
    num = int(input('Mostrar notas de qual aluno? [999 para finalizar] '))
    if num == 999:
        print('Finalizando')
        break
    if num <= len(dados) - 1:
        print(f'Notas de {dados[num][0]} são {dados[num][1]}')
print(f'{'Volte sempre':-^60}')
