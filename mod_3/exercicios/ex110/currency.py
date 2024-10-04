def aumentar(preço=0, taxa=0, formatado=False):
    res = preço + (preço * taxa/100)
    return res if formatado is False else moeda(res)


def diminuir(preço=0, taxa=0, formatado=False):
    res = preço - (preço * taxa/100)
    return res if formatado is False else moeda(res)


def dobro(preço=0, formatado=False):
    res = preço * 2
    return res if not formatado else moeda(res)


def metade(preço=0, formatado=False):
    res = preço / 2
    return res if formatado is False else moeda(res)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:>.2f}'.replace('.', ',')


def resumo(preço=0, taxa_a=15, taxa_r=5):
    print('-=' * 20)
    print('Resumo do Valor'.center(40))
    print('-=' * 20)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'Com {taxa_a}% de aumento: \t{aumentar(preço, taxa_a, True)}')
    print(f'Com {taxa_r}% de redução: \t{diminuir(preço, taxa_r, True)}')
    print('-=' * 20)
