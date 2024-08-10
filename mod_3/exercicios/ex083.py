express = str(input('Digite a expressão: '))
pilha = list()

for e in express:
    if e == '(':
        pilha.append('(')
    elif e ==')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão é válida!')
else:
    print('Sua expressão é inválida!')
