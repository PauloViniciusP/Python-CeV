nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
nota3 = float(input('Terceira nota: '))
media = (nota1 + nota2 + nota3) / 3

if media < 5:
    print('Aluno reprovado.')
elif 5 <= media < 7:
    print('Aluno em recuperação.')
elif 7 <= media <= 10:
    print('Aluno aprovado!')
else:
    print('Notas inválidas, tente novamente.')