def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['menor'] = min(n)
    r['maior'] = max(n)
    r['média'] = sum(n)/len(n)
    
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'Boa'
        elif r['média'] >= 5:
            r['situação'] = 'Razoável'
        else:
            r['situação'] = 'Ruim'
    return r


# main program
resp = notas(4.5, 5.6, 9, 10, sit=True)
print(resp)
