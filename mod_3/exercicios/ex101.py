def voto(ano):
    from datetime import date
    anoAtual = date.today().year
    idade = anoAtual - ano
    if idade >= 65 or 16 <= idade < 18:
        return f' Com {idade} anos: Voto Opcional!'
    elif 18 <= idade < 65:
        return f'Com {idade} anos: Voto Obrigatório!'
    else:
        return f'Com {idade} anos: Voto Negado!'


print('-=-' * 10)
anoNasc = int(input('Digite o ano de nascimento: '))

print(voto(anoNasc))

